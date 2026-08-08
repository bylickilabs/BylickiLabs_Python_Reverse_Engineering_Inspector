from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class SymbolInfo:
    name: str
    kind: str
    file: str
    line: int
    end_line: int
    parent: str = ""
    parameters: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)
    complexity: int = 1
    calls: list[str] = field(default_factory=list)

@dataclass
class ImportInfo:
    module: str
    name: str
    alias: str
    file: str
    line: int
    category: str

@dataclass
class CallInfo:
    caller: str
    callee: str
    file: str
    line: int

@dataclass
class RiskFinding:
    code: str
    severity: str
    file: str
    line: int
    symbol: str = ""
    evidence: str = ""

@dataclass
class FileAnalysis:
    relative_path: str
    absolute_path: str
    lines: int = 0
    code_lines: int = 0
    comment_lines: int = 0
    blank_lines: int = 0
    symbols: list[SymbolInfo] = field(default_factory=list)
    imports: list[ImportInfo] = field(default_factory=list)
    calls: list[CallInfo] = field(default_factory=list)
    risks: list[RiskFinding] = field(default_factory=list)
    syntax_error: str = ""

@dataclass
class ProjectMetrics:
    files: int = 0
    modules: int = 0
    classes: int = 0
    functions: int = 0
    methods: int = 0
    imports: int = 0
    dependencies: int = 0
    code_lines: int = 0
    total_lines: int = 0
    comment_lines: int = 0
    blank_lines: int = 0
    average_complexity: float = 0.0
    median_complexity: float = 0.0
    p95_complexity: float = 0.0
    std_complexity: float = 0.0
    max_complexity: int = 0
    complexity_outliers: int = 0
    risk_findings: int = 0

@dataclass
class ComplexityAnomaly:
    symbol: str
    file: str
    line: int
    complexity: int
    z_score: float

@dataclass
class AnalysisResult:
    project_name: str
    project_path: str
    analyzed_at: str
    python_files: list[FileAnalysis] = field(default_factory=list)
    metrics: ProjectMetrics = field(default_factory=ProjectMetrics)
    dependencies: dict[str, dict[str, Any]] = field(default_factory=dict)
    anomalies: list[ComplexityAnomaly] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
