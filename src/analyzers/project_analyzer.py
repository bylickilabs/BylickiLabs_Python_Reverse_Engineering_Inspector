from __future__ import annotations

import ast
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Callable

import numpy as np
from scipy import stats

from src.config import EXCLUDED_DIRS
from src.models import (
    AnalysisResult,
    CallInfo,
    ComplexityAnomaly,
    FileAnalysis,
    ImportInfo,
    ProjectMetrics,
    RiskFinding,
    SymbolInfo,
)


def full_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id

    if isinstance(node, ast.Attribute):
        base = full_name(node.value)
        return f"{base}.{node.attr}" if base else node.attr

    return ""


def decorator_name(node: ast.AST) -> str:
    name = full_name(node)

    if name:
        return name

    if hasattr(ast, "unparse"):
        try:
            return ast.unparse(node)
        except Exception:
            pass

    return node.__class__.__name__


class ComplexityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.score = 1

    def visit_If(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_AsyncFor(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_IfExp(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_Assert(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_comprehension(self, node):
        self.score += 1
        self.generic_visit(node)

    def visit_BoolOp(self, node):
        self.score += max(1, len(node.values) - 1)
        self.generic_visit(node)

    def visit_Try(self, node):
        self.score += len(node.handlers) + (1 if node.orelse else 0)
        self.generic_visit(node)

    def visit_Match(self, node):
        self.score += len(node.cases)
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        return

    def visit_AsyncFunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return


def complexity_of(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> int:
    visitor = ComplexityVisitor()

    for statement in node.body:
        visitor.visit(statement)

    return visitor.score


class DirectCallVisitor(ast.NodeVisitor):
    def __init__(self):
        self.calls = []

    def visit_Call(self, node):
        name = full_name(node.func)

        if name:
            self.calls.append(
                (
                    name,
                    getattr(node, "lineno", 0),
                )
            )

        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        return

    def visit_AsyncFunctionDef(self, node):
        return

    def visit_ClassDef(self, node):
        return


def direct_calls(node):
    visitor = DirectCallVisitor()

    for statement in node.body:
        visitor.visit(statement)

    return visitor.calls


class FileVisitor(ast.NodeVisitor):
    SECRET_NAMES = {
        "password",
        "passwd",
        "pwd",
        "secret",
        "token",
        "api_key",
        "apikey",
        "access_token",
        "private_key",
        "client_secret",
    }

    def __init__(
        self,
        file_analysis: FileAnalysis,
        internal_roots: set[str],
    ):
        self.fa = file_analysis
        self.internal_roots = internal_roots
        self.scope = []
        self.class_depth = 0

    def parent(self):
        return ".".join(self.scope)

    def category(self, module):
        root = (module or "").split(".")[0]

        if root in self.internal_roots:
            return "internal"

        if root in getattr(sys, "stdlib_module_names", set()):
            return "standard"

        return "third_party"

    def params(self, node):
        args = (
            list(node.args.posonlyargs)
            + list(node.args.args)
            + list(node.args.kwonlyargs)
        )

        names = [argument.arg for argument in args]

        if node.args.vararg:
            names.append("*" + node.args.vararg.arg)

        if node.args.kwarg:
            names.append("**" + node.args.kwarg.arg)

        return names

    def add_function(
        self,
        node,
        is_async=False,
    ):
        parent = self.parent()

        kind = "method" if self.class_depth else "function"

        if is_async:
            kind = (
                "async_method"
                if self.class_depth
                else "async_function"
            )

        calls = direct_calls(node)

        symbol = SymbolInfo(
            node.name,
            kind,
            self.fa.relative_path,
            node.lineno,
            getattr(
                node,
                "end_lineno",
                node.lineno,
            ),
            parent,
            self.params(node),
            [
                decorator_name(decorator)
                for decorator in node.decorator_list
            ],
            complexity_of(node),
            sorted(
                {
                    call[0]
                    for call in calls
                }
            ),
        )

        self.fa.symbols.append(symbol)

        caller = (
            f"{parent + '.' if parent else ''}{node.name}"
        )

        for callee, line in calls:
            self.fa.calls.append(
                CallInfo(
                    caller,
                    callee,
                    self.fa.relative_path,
                    line,
                )
            )

        self.scope.append(node.name)

        self.generic_visit(node)

        self.scope.pop()

    def visit_FunctionDef(self, node):
        self.add_function(node, False)

    def visit_AsyncFunctionDef(self, node):
        self.add_function(node, True)

    def visit_ClassDef(self, node):
        self.fa.symbols.append(
            SymbolInfo(
                node.name,
                "class",
                self.fa.relative_path,
                node.lineno,
                getattr(
                    node,
                    "end_lineno",
                    node.lineno,
                ),
                self.parent(),
                decorators=[
                    decorator_name(decorator)
                    for decorator in node.decorator_list
                ],
            )
        )

        self.scope.append(node.name)
        self.class_depth += 1

        self.generic_visit(node)

        self.class_depth -= 1
        self.scope.pop()

    def visit_Import(self, node):
        for alias in node.names:
            self.fa.imports.append(
                ImportInfo(
                    alias.name,
                    alias.name,
                    alias.asname or "",
                    self.fa.relative_path,
                    node.lineno,
                    self.category(alias.name),
                )
            )

    def visit_ImportFrom(self, node):
        module = node.module or ""

        category = (
            self.category(module)
            if module
            else "internal"
        )

        for alias in node.names:
            self.fa.imports.append(
                ImportInfo(
                    module,
                    alias.name,
                    alias.asname or "",
                    self.fa.relative_path,
                    node.lineno,
                    category,
                )
            )

    def visit_Call(self, node):
        name = full_name(node.func)

        mapping = {
            "eval": (
                "eval",
                "high",
            ),
            "exec": (
                "exec",
                "high",
            ),
            "compile": (
                "compile",
                "medium",
            ),
            "os.system": (
                "os_system",
                "high",
            ),
            "pickle.load": (
                "pickle",
                "high",
            ),
            "pickle.loads": (
                "pickle",
                "high",
            ),
            "yaml.load": (
                "yaml_load",
                "high",
            ),
            "tempfile.mktemp": (
                "tempfile_mktemp",
                "medium",
            ),
        }

        if name in mapping:
            code, severity = mapping[name]

            self.fa.risks.append(
                RiskFinding(
                    code,
                    severity,
                    self.fa.relative_path,
                    node.lineno,
                    self.parent(),
                    name,
                )
            )

        if name.startswith("subprocess."):
            self.fa.risks.append(
                RiskFinding(
                    "subprocess",
                    "medium",
                    self.fa.relative_path,
                    node.lineno,
                    self.parent(),
                    name,
                )
            )

            for keyword in node.keywords:
                if (
                    keyword.arg == "shell"
                    and isinstance(
                        keyword.value,
                        ast.Constant,
                    )
                    and keyword.value.value is True
                ):
                    self.fa.risks.append(
                        RiskFinding(
                            "shell_true",
                            "high",
                            self.fa.relative_path,
                            node.lineno,
                            self.parent(),
                            f"{name}(..., shell=True)",
                        )
                    )

        if (
            name.startswith("requests.")
            or name.endswith(".request")
            or name.endswith(".get")
            or name.endswith(".post")
        ):
            for keyword in node.keywords:
                if (
                    keyword.arg == "verify"
                    and isinstance(
                        keyword.value,
                        ast.Constant,
                    )
                    and keyword.value.value is False
                ):
                    self.fa.risks.append(
                        RiskFinding(
                            "verify_false",
                            "high",
                            self.fa.relative_path,
                            node.lineno,
                            self.parent(),
                            "verify=False",
                        )
                    )

        self.generic_visit(node)

    def visit_Assign(self, node):
        if (
            isinstance(node.value, ast.Constant)
            and isinstance(node.value.value, str)
        ):
            for target in node.targets:
                if (
                    isinstance(target, ast.Name)
                    and target.id.lower()
                    in self.SECRET_NAMES
                ):
                    value = node.value.value

                    masked = (
                        value[:2] + "***"
                        if value
                        else "***"
                    )

                    self.fa.risks.append(
                        RiskFinding(
                            "hardcoded_secret",
                            "high",
                            self.fa.relative_path,
                            node.lineno,
                            self.parent(),
                            f"{target.id} = {masked!r}",
                        )
                    )

        self.generic_visit(node)


class ProjectAnalyzer:
    def __init__(
        self,
        cancel_check: Callable[[], bool] | None = None,
    ):
        self.cancel_check = (
            cancel_check
            or (lambda: False)
        )

    def python_files(
        self,
        root: Path,
    ):
        found = []

        for pattern in (
            "*.py",
            "*.pyw",
        ):
            for path in root.rglob(pattern):
                if (
                    path.is_file()
                    and not any(
                        part in EXCLUDED_DIRS
                        for part in path.parts
                    )
                ):
                    found.append(path)

        return sorted(set(found))

    def internal_roots(
        self,
        root,
        files,
    ):
        roots = set()

        for file in files:
            relative = file.relative_to(root)

            roots.add(
                file.stem
                if len(relative.parts) == 1
                else relative.parts[0]
            )

        return roots

    def line_stats(
        self,
        source,
    ):
        lines = source.splitlines()

        blank = 0
        comment = 0
        code = 0

        for line in lines:
            stripped = line.strip()

            if not stripped:
                blank += 1

            elif stripped.startswith("#"):
                comment += 1

            else:
                code += 1

        return (
            len(lines),
            code,
            comment,
            blank,
        )

    def analyze(
        self,
        project_path: str,
        progress=None,
    ):
        root = Path(project_path).resolve()

        files = self.python_files(root)

        if not files:
            raise ValueError(
                "NO_PYTHON_FILES"
            )

        internal = self.internal_roots(
            root,
            files,
        )

        result = AnalysisResult(
            root.name,
            str(root),
            datetime.now()
            .astimezone()
            .isoformat(
                timespec="seconds"
            ),
        )

        for index, path in enumerate(
            files,
            1,
        ):
            if self.cancel_check():
                raise InterruptedError(
                    "CANCELLED"
                )

            relative = str(
                path.relative_to(root)
            ).replace(
                "\\",
                "/",
            )

            if progress:
                progress(
                    int(
                        (index - 1)
                        / len(files)
                        * 80
                    ),
                    relative,
                )

            file_analysis = FileAnalysis(
                relative,
                str(path),
            )

            source = path.read_text(
                encoding="utf-8",
                errors="replace",
            )

            (
                file_analysis.lines,
                file_analysis.code_lines,
                file_analysis.comment_lines,
                file_analysis.blank_lines,
            ) = self.line_stats(source)

            try:
                tree = ast.parse(
                    source,
                    filename=str(path),
                )

                FileVisitor(
                    file_analysis,
                    internal,
                ).visit(tree)

            except SyntaxError as error:
                file_analysis.syntax_error = (
                    f"{error.msg} "
                    f"(line {error.lineno})"
                )

            except Exception as error:
                file_analysis.syntax_error = (
                    f"{type(error).__name__}: "
                    f"{error}"
                )

            result.python_files.append(
                file_analysis
            )

        if progress:
            progress(
                82,
                "metrics",
            )

        self.build_dependencies(result)
        self.build_metrics(result)
        self.build_anomalies(result)

        if progress:
            progress(
                100,
                "done",
            )

        return result

    def build_dependencies(
        self,
        result,
    ):
        dependency_files = defaultdict(set)
        dependency_categories = {}
        dependency_uses = Counter()

        for file_analysis in result.python_files:
            for imported in file_analysis.imports:
                key = (
                    imported.module
                    or imported.name
                )

                root = (
                    key.split(".")[0]
                    if key
                    else imported.name.split(".")[0]
                )

                if not root:
                    continue

                dependency_files[root].add(
                    file_analysis.relative_path
                )

                dependency_categories[root] = (
                    imported.category
                )

                dependency_uses[root] += 1

        result.dependencies = {
            name: {
                "category": dependency_categories.get(
                    name,
                    "third_party",
                ),
                "files": sorted(
                    dependency_files[name]
                ),
                "uses": dependency_uses[name],
            }
            for name in sorted(
                dependency_files
            )
        }

    def build_metrics(
        self,
        result,
    ):
        symbols = [
            symbol
            for file_analysis
            in result.python_files
            for symbol
            in file_analysis.symbols
        ]

        functions = [
            symbol
            for symbol in symbols
            if symbol.kind
            in {
                "function",
                "async_function",
            }
        ]

        methods = [
            symbol
            for symbol in symbols
            if symbol.kind
            in {
                "method",
                "async_method",
            }
        ]

        values = (
            np.array(
                [
                    symbol.complexity
                    for symbol
                    in functions + methods
                ],
                dtype=float,
            )
            if functions or methods
            else np.array(
                [],
                dtype=float,
            )
        )

        metrics = ProjectMetrics(
            files=len(
                result.python_files
            ),
            modules=len(
                result.python_files
            ),
            classes=sum(
                symbol.kind == "class"
                for symbol in symbols
            ),
            functions=len(functions),
            methods=len(methods),
            imports=sum(
                len(file_analysis.imports)
                for file_analysis
                in result.python_files
            ),
            dependencies=len(
                result.dependencies
            ),
            code_lines=sum(
                file_analysis.code_lines
                for file_analysis
                in result.python_files
            ),
            total_lines=sum(
                file_analysis.lines
                for file_analysis
                in result.python_files
            ),
            comment_lines=sum(
                file_analysis.comment_lines
                for file_analysis
                in result.python_files
            ),
            blank_lines=sum(
                file_analysis.blank_lines
                for file_analysis
                in result.python_files
            ),
            risk_findings=sum(
                len(file_analysis.risks)
                for file_analysis
                in result.python_files
            ),
        )

        if values.size:
            metrics.average_complexity = float(
                np.mean(values)
            )

            metrics.median_complexity = float(
                np.median(values)
            )

            metrics.p95_complexity = float(
                np.percentile(
                    values,
                    95,
                )
            )

            metrics.std_complexity = float(
                np.std(values)
            )

            metrics.max_complexity = int(
                np.max(values)
            )

        result.metrics = metrics

    def build_anomalies(
        self,
        result,
    ):
        callables = [
            symbol
            for file_analysis
            in result.python_files
            for symbol
            in file_analysis.symbols
            if symbol.kind
            in {
                "function",
                "async_function",
                "method",
                "async_method",
            }
        ]

        if len(callables) < 3:
            result.anomalies = []
            return

        values = np.array(
            [
                symbol.complexity
                for symbol in callables
            ],
            dtype=float,
        )

        z_scores = (
            np.zeros_like(values)
            if np.std(values) == 0
            else stats.zscore(
                values,
                nan_policy="omit",
            )
        )

        result.anomalies = sorted(
            [
                ComplexityAnomaly(
                    (
                        f"{symbol.parent + '.' if symbol.parent else ''}"
                        f"{symbol.name}"
                    ),
                    symbol.file,
                    symbol.line,
                    symbol.complexity,
                    float(z_score),
                )
                for symbol, z_score
                in zip(
                    callables,
                    z_scores,
                )
                if (
                    np.isfinite(z_score)
                    and z_score >= 2.0
                )
            ],
            key=lambda anomaly: anomaly.z_score,
            reverse=True,
        )

        result.metrics.complexity_outliers = len(
            result.anomalies
        )