from __future__ import annotations

import csv
import html
import json
from pathlib import Path

from src.models import AnalysisResult


LABELS = {
    "de": {
        "section": "Bereich",
        "name": "Name",
        "type": "Typ/Schweregrad",
        "file": "Datei",
        "line": "Zeile",
        "details": "Details",
        "symbol": "Symbol",
        "risk": "Risiko",
        "report": "BPREI Analysebericht",
        "project": "Projekt",
        "path": "Pfad",
        "analyzed": "Analysiert",
        "metrics": "Metriken",
        "files": "Dateien",
        "classes": "Klassen",
        "functions": "Funktionen & Methoden",
        "dependencies": "Abhängigkeiten",
        "code_lines": "Codezeilen",
        "risks": "Risikobefunde",
        "avg": "Durchschnittliche Komplexität",
        "p95": "95. Perzentil",
        "risk_findings": "Risikobefunde",
        "none": "Keine",
    },
    "en": {
        "section": "Section",
        "name": "Name",
        "type": "Type/Severity",
        "file": "File",
        "line": "Line",
        "details": "Details",
        "symbol": "Symbol",
        "risk": "Risk",
        "report": "BPREI Analysis Report",
        "project": "Project",
        "path": "Path",
        "analyzed": "Analyzed",
        "metrics": "Metrics",
        "files": "Files",
        "classes": "Classes",
        "functions": "Functions & Methods",
        "dependencies": "Dependencies",
        "code_lines": "Code lines",
        "risks": "Risk findings",
        "avg": "Average complexity",
        "p95": "95th percentile",
        "risk_findings": "Risk Findings",
        "none": "None",
    },
}


def export_result(
    result: AnalysisResult,
    destination: str,
    language: str = "de",
):
    path = Path(destination)

    language = (
        language
        if language in LABELS
        else "de"
    )

    suffix = path.suffix.lower()

    if suffix == ".json":
        path.write_text(
            json.dumps(
                result.to_dict(),
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        return

    if suffix == ".csv":
        return _csv(
            result,
            path,
            language,
        )

    if suffix == ".html":
        return _html(
            result,
            path,
            language,
        )

    if suffix == ".md":
        return _md(
            result,
            path,
            language,
        )

    raise ValueError(
        f"Unsupported export format: {path.suffix}"
    )


def _safe(value):
    text = (
        ""
        if value is None
        else str(value)
    )

    if text.startswith(
        (
            "=",
            "+",
            "-",
            "@",
            "\t",
            "\r",
        )
    ):
        return "'" + text

    return text


def _csv(
    result,
    path,
    language,
):
    labels = LABELS[language]

    with path.open(
        "w",
        newline="",
        encoding="utf-8-sig",
    ) as file:
        writer = csv.writer(
            file,
            delimiter=";",
        )

        writer.writerow(
            [
                labels["section"],
                labels["name"],
                labels["type"],
                labels["file"],
                labels["line"],
                labels["details"],
            ]
        )

        for file_analysis in result.python_files:
            for symbol in file_analysis.symbols:
                writer.writerow(
                    [
                        labels["symbol"],
                        _safe(symbol.name),
                        symbol.kind,
                        file_analysis.relative_path,
                        symbol.line,
                        f"complexity={symbol.complexity}",
                    ]
                )

            for risk in file_analysis.risks:
                writer.writerow(
                    [
                        labels["risk"],
                        risk.code,
                        risk.severity,
                        file_analysis.relative_path,
                        risk.line,
                        _safe(risk.evidence),
                    ]
                )


def _html(
    result,
    path,
    language,
):
    labels = LABELS[language]
    metrics = result.metrics

    risks = [
        risk
        for file_analysis in result.python_files
        for risk in file_analysis.risks
    ]

    rows = "".join(
        f"""
        <tr>
            <td>{html.escape(risk.severity)}</td>
            <td>{html.escape(risk.code)}</td>
            <td>{html.escape(risk.file)}</td>
            <td>{risk.line}</td>
            <td>{html.escape(risk.evidence)}</td>
        </tr>
        """
        for risk in risks
    )

    if not rows:
        rows = f"""
        <tr>
            <td colspan="5">
                {html.escape(labels["none"])}
            </td>
        </tr>
        """

    document = f"""<!DOCTYPE html>
<html lang="{language}">
<head>
    <meta charset="utf-8">
    <meta
        name="viewport"
        content="width=device-width, initial-scale=1"
    >

    <title>
        {html.escape(result.project_name)} | BPREI
    </title>

    <style>
        body {{
            font-family: "Segoe UI", Arial, sans-serif;
            background: #0f141a;
            color: #e8edf2;
            margin: 40px;
        }}

        h1,
        h2 {{
            color: #ffffff;
        }}

        .subtitle {{
            color: #9fb0c0;
            margin-bottom: 24px;
        }}

        .card {{
            background: #171e26;
            border: 1px solid #26313d;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 24px;
        }}

        .metrics {{
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
        }}

        .metric {{
            background: #111820;
            border: 1px solid #26313d;
            border-radius: 8px;
            padding: 14px;
        }}

        .metric-label {{
            color: #9fb0c0;
            font-size: 13px;
        }}

        .metric-value {{
            font-size: 22px;
            font-weight: 700;
            margin-top: 6px;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            background: #171e26;
            border: 1px solid #26313d;
        }}

        th,
        td {{
            padding: 10px;
            border-bottom: 1px solid #26313d;
            text-align: left;
            vertical-align: top;
        }}

        th {{
            background: #1d2731;
        }}

        tr:last-child td {{
            border-bottom: none;
        }}
    </style>
</head>

<body>
    <h1>
        {html.escape(labels["report"])}
    </h1>

    <div class="subtitle">
        {html.escape(result.project_name)}
        ·
        {html.escape(result.analyzed_at)}
    </div>

    <div class="card">
        <h2>
            {html.escape(labels["metrics"])}
        </h2>

        <div class="metrics">
            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["files"])}
                </div>
                <div class="metric-value">
                    {metrics.files}
                </div>
            </div>

            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["classes"])}
                </div>
                <div class="metric-value">
                    {metrics.classes}
                </div>
            </div>

            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["functions"])}
                </div>
                <div class="metric-value">
                    {metrics.functions + metrics.methods}
                </div>
            </div>

            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["dependencies"])}
                </div>
                <div class="metric-value">
                    {metrics.dependencies}
                </div>
            </div>

            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["risks"])}
                </div>
                <div class="metric-value">
                    {metrics.risk_findings}
                </div>
            </div>

            <div class="metric">
                <div class="metric-label">
                    {html.escape(labels["avg"])}
                </div>
                <div class="metric-value">
                    {metrics.average_complexity:.2f}
                </div>
            </div>
        </div>
    </div>

    <h2>
        {html.escape(labels["risk_findings"])}
    </h2>

    <table>
        <thead>
            <tr>
                <th>
                    {html.escape(labels["type"])}
                </th>
                <th>
                    {html.escape(labels["name"])}
                </th>
                <th>
                    {html.escape(labels["file"])}
                </th>
                <th>
                    {html.escape(labels["line"])}
                </th>
                <th>
                    {html.escape(labels["details"])}
                </th>
            </tr>
        </thead>

        <tbody>
            {rows}
        </tbody>
    </table>
</body>
</html>
"""

    path.write_text(
        document,
        encoding="utf-8",
    )


def _md(
    result,
    path,
    language,
):
    labels = LABELS[language]
    metrics = result.metrics

    risks = [
        risk
        for file_analysis in result.python_files
        for risk in file_analysis.risks
    ]

    lines = [
        f"# {labels['report']}",
        "",
        f"**{labels['project']}:** "
        f"{result.project_name}",
        f"**{labels['path']}:** "
        f"`{result.project_path}`",
        f"**{labels['analyzed']}:** "
        f"{result.analyzed_at}",
        "",
        f"## {labels['metrics']}",
        "",
        f"- {labels['files']}: "
        f"{metrics.files}",
        f"- {labels['classes']}: "
        f"{metrics.classes}",
        f"- {labels['functions']}: "
        f"{metrics.functions + metrics.methods}",
        f"- {labels['dependencies']}: "
        f"{metrics.dependencies}",
        f"- {labels['code_lines']}: "
        f"{metrics.code_lines}",
        f"- {labels['risks']}: "
        f"{metrics.risk_findings}",
        f"- {labels['avg']}: "
        f"{metrics.average_complexity:.2f}",
        f"- {labels['p95']}: "
        f"{metrics.p95_complexity:.2f}",
        "",
        f"## {labels['risk_findings']}",
        "",
    ]

    if risks:
        lines.extend(
            [
                (
                    f"- **{risk.severity.upper()}** "
                    f"`{risk.code}` "
                    f"— `{risk.file}:{risk.line}` "
                    f"— {risk.evidence}"
                )
                for risk in risks
            ]
        )

    else:
        lines.append(
            f"- {labels['none']}"
        )

    path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )