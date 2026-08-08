from __future__ import annotations

TRANSLATIONS = {
    "de": {
        "app.subtitle": "Statische Codeanalyse & Reverse Engineering für Python",
        "nav.dashboard": "Dashboard",
        "nav.explorer": "Projekt-Explorer",
        "nav.dependencies": "Abhängigkeiten",
        "nav.calls": "Funktionsaufrufe",
        "nav.complexity": "Komplexität",
        "nav.risks": "Risikoanalyse",
        "nav.bytecode": "Bytecode",
        "nav.history": "Verlauf",
        "button.open_project": "Projekt öffnen",
        "button.analyze": "Analysieren",
        "button.export": "Exportieren",
        "button.cancel": "Abbrechen",
        "button.refresh": "Aktualisieren",
        "button.info": "Info",
        "button.close": "Schließen",
        "button.language": "English",
        "status.ready": "Bereit",
        "status.loading": "Projekt wird analysiert …",
        "status.done": "Analyse abgeschlossen",
        "status.failed": "Analyse fehlgeschlagen",
        "status.cancelled": "Analyse abgebrochen",
        "dialog.select_project": "Python-Projekt auswählen",
        "dialog.select_export": "Bericht exportieren",
        "dialog.no_project": "Bitte zuerst ein Python-Projekt auswählen.",
        "dialog.no_result": "Es liegt noch kein Analyseergebnis vor.",
        "dialog.error": "Fehler",
        "dialog.success": "Erfolgreich",
        "dialog.export_done": "Der Bericht wurde erfolgreich exportiert.",
        "dialog.project_invalid": "Der ausgewählte Ordner enthält keine Python-Dateien.",
        "dashboard.files": "Python-Dateien",
        "dashboard.classes": "Klassen",
        "dashboard.functions": "Funktionen & Methoden",
        "dashboard.dependencies": "Abhängigkeiten",
        "dashboard.code_lines": "Codezeilen",
        "dashboard.risks": "Risiken",
        "dashboard.avg_complexity": "Ø Komplexität",
        "dashboard.max_complexity": "Max. Komplexität",
        "dashboard.outliers": "Auffälligkeiten",
        "dashboard.overview": "Projektübersicht",
        "dashboard.anomalies": "Statistische Auffälligkeiten",
        "explorer.files": "Projektstruktur",
        "explorer.source": "Quellcode",
        "explorer.details": "Symbolinformationen",
        "explorer.file_stats": "{lines} Zeilen\n{symbols} Symbole\n{imports} Imports",
        "explorer.syntax": "Syntaxfehler: {error}",
        "detail.kind": "Typ",
        "detail.file": "Datei",
        "detail.line": "Zeile",
        "detail.lines": "Zeilen",
        "detail.parameters": "Parameter",
        "detail.decorators": "Decorator",
        "detail.calls": "Aufrufe",
        "detail.complexity": "Komplexität",
        "kind.class": "Klasse",
        "kind.function": "Funktion",
        "kind.async_function": "Asynchrone Funktion",
        "kind.method": "Methode",
        "kind.async_method": "Asynchrone Methode",
        "table.module": "Modul",
        "table.type": "Typ",
        "table.file": "Datei",
        "table.line": "Zeile",
        "table.uses": "Verwendungen",
        "table.caller": "Aufrufer",
        "table.callee": "Aufgerufenes Ziel",
        "table.symbol": "Symbol",
        "table.complexity": "Komplexität",
        "table.zscore": "Z-Wert",
        "table.severity": "Schweregrad",
        "table.finding": "Befund",
        "table.evidence": "Nachweis",
        "table.date": "Datum",
        "table.path": "Pfad",
        "table.summary": "Zusammenfassung",
        "table.project": "Projekt",
        "history.summary": "{files} Dateien | {deps} Abhängigkeiten | {risks} Risiken | ØK={complexity:.2f}",
        "dep.standard": "Standardbibliothek",
        "dep.internal": "Projektintern",
        "dep.third_party": "Drittanbieter",
        "severity.low": "Niedrig",
        "severity.medium": "Mittel",
        "severity.high": "Hoch",
        "severity.critical": "Kritisch",
        "severity.info": "Information",
        "risk.eval": "Dynamische Codeausführung mit eval()",
        "risk.exec": "Dynamische Codeausführung mit exec()",
        "risk.os_system": "Systembefehl über os.system()",
        "risk.subprocess": "Externer Prozessaufruf",
        "risk.shell_true": "Subprocess mit shell=True",
        "risk.pickle": "Potentiell unsichere Pickle-Deserialisierung",
        "risk.yaml_load": "Potentiell unsicherer yaml.load()-Aufruf",
        "risk.verify_false": "TLS-Zertifikatsprüfung wurde deaktiviert",
        "risk.hardcoded_secret": "Möglicherweise fest hinterlegtes Geheimnis",
        "risk.tempfile_mktemp": "Unsichere temporäre Dateierzeugung mit mktemp()",
        "risk.compile": "Dynamische Code-Kompilierung mit compile()",
        "bytecode.help": (
            "Wähle im Projekt-Explorer eine Python-Datei aus. Der Bytecode wird nur "
            "kompiliert und disassembliert; das Zielprojekt wird nicht ausgeführt."
        ),
        "bytecode.error": "Bytecode konnte nicht erzeugt werden.",
        "about.title": "Über die Anwendung",
        "about.heading": "BylickiLabs Python Reverse Engineering Inspector",
        "about.body": (
            "Der BylickiLabs Python Reverse Engineering Inspector ist eine Business-Anwendung "
            "zur statischen Untersuchung und strukturellen Zerlegung von Python-Projekten. "
            "Analysiert werden Quellcode, Module, Klassen, Funktionen, Imports, Abhängigkeiten, "
            "Funktionsaufrufe, Komplexität und ausgewählte sicherheitsrelevante Muster.\n\n"
            "NumPy berechnet statistische Projektmetriken wie Mittelwert, Median, "
            "Standardabweichung und Perzentile. SciPy ergänzt dies um eine Z-Score-basierte "
            "Erkennung auffälliger Komplexitätswerte.\n\n"
            "Das untersuchte Projekt wird nicht importiert oder ausgeführt. Die Analyse basiert "
            "auf dem Python-AST. Die Bytecode-Ansicht kompiliert Quelltext nur zu Codeobjekten "
            "und disassembliert diese ohne Ausführung.\n\n"
            "Kernbereiche:\n"
            "• Projekt- und Symbolstruktur\n"
            "• Abhängigkeitsanalyse\n"
            "• Call-Graph-Auswertung\n"
            "• Komplexitätsmetriken\n"
            "• Risk-Pattern-Analyse\n"
            "• NumPy-/SciPy-Statistik\n"
            "• Bytecode-Inspektion\n"
            "• SQLite-Verlauf\n"
            "• JSON-, CSV-, HTML- und Markdown-Export\n"
            "• Vollständige deutsche und englische Oberfläche\n\n"
            "Version: {version}\n"
            "Entwickler: {author}"
        ),
        "export.filter": "JSON (*.json);;CSV (*.csv);;HTML (*.html);;Markdown (*.md)",
    },
    "en": {
        "app.subtitle": "Static Code Analysis & Reverse Engineering for Python",
        "nav.dashboard": "Dashboard",
        "nav.explorer": "Project Explorer",
        "nav.dependencies": "Dependencies",
        "nav.calls": "Function Calls",
        "nav.complexity": "Complexity",
        "nav.risks": "Risk Analysis",
        "nav.bytecode": "Bytecode",
        "nav.history": "History",
        "button.open_project": "Open Project",
        "button.analyze": "Analyze",
        "button.export": "Export",
        "button.cancel": "Cancel",
        "button.refresh": "Refresh",
        "button.info": "Info",
        "button.close": "Close",
        "button.language": "German",
        "status.ready": "Ready",
        "status.loading": "Analyzing project …",
        "status.done": "Analysis completed",
        "status.failed": "Analysis failed",
        "status.cancelled": "Analysis cancelled",
        "dialog.select_project": "Select Python project",
        "dialog.select_export": "Export report",
        "dialog.no_project": "Please select a Python project first.",
        "dialog.no_result": "No analysis result is available yet.",
        "dialog.error": "Error",
        "dialog.success": "Success",
        "dialog.export_done": "The report was exported successfully.",
        "dialog.project_invalid": "The selected folder does not contain Python files.",
        "dashboard.files": "Python Files",
        "dashboard.classes": "Classes",
        "dashboard.functions": "Functions & Methods",
        "dashboard.dependencies": "Dependencies",
        "dashboard.code_lines": "Code Lines",
        "dashboard.risks": "Risks",
        "dashboard.avg_complexity": "Avg. Complexity",
        "dashboard.max_complexity": "Max. Complexity",
        "dashboard.outliers": "Anomalies",
        "dashboard.overview": "Project Overview",
        "dashboard.anomalies": "Statistical Anomalies",
        "explorer.files": "Project Structure",
        "explorer.source": "Source Code",
        "explorer.details": "Symbol Information",
        "explorer.file_stats": "{lines} lines\n{symbols} symbols\n{imports} imports",
        "explorer.syntax": "Syntax error: {error}",
        "detail.kind": "Type",
        "detail.file": "File",
        "detail.line": "Line",
        "detail.lines": "Lines",
        "detail.parameters": "Parameters",
        "detail.decorators": "Decorators",
        "detail.calls": "Calls",
        "detail.complexity": "Complexity",
        "kind.class": "Class",
        "kind.function": "Function",
        "kind.async_function": "Async Function",
        "kind.method": "Method",
        "kind.async_method": "Async Method",
        "table.module": "Module",
        "table.type": "Type",
        "table.file": "File",
        "table.line": "Line",
        "table.uses": "Uses",
        "table.caller": "Caller",
        "table.callee": "Callee",
        "table.symbol": "Symbol",
        "table.complexity": "Complexity",
        "table.zscore": "Z-Score",
        "table.severity": "Severity",
        "table.finding": "Finding",
        "table.evidence": "Evidence",
        "table.date": "Date",
        "table.path": "Path",
        "table.summary": "Summary",
        "table.project": "Project",
        "history.summary": "{files} files | {deps} dependencies | {risks} risks | AvgC={complexity:.2f}",
        "dep.standard": "Standard Library",
        "dep.internal": "Internal",
        "dep.third_party": "Third Party",
        "severity.low": "Low",
        "severity.medium": "Medium",
        "severity.high": "High",
        "severity.critical": "Critical",
        "severity.info": "Information",
        "risk.eval": "Dynamic code execution using eval()",
        "risk.exec": "Dynamic code execution using exec()",
        "risk.os_system": "System command through os.system()",
        "risk.subprocess": "External process invocation",
        "risk.shell_true": "Subprocess invocation with shell=True",
        "risk.pickle": "Potentially unsafe Pickle deserialization",
        "risk.yaml_load": "Potentially unsafe yaml.load() invocation",
        "risk.verify_false": "TLS certificate verification is disabled",
        "risk.hardcoded_secret": "Possible hardcoded secret",
        "risk.tempfile_mktemp": "Unsafe temporary file creation using mktemp()",
        "risk.compile": "Dynamic code compilation using compile()",
        "bytecode.help": (
            "Select a Python file in the Project Explorer. Bytecode is only compiled and "
            "disassembled; the target project is not executed."
        ),
        "bytecode.error": "Bytecode could not be generated.",
        "about.title": "About",
        "about.heading": "BylickiLabs Python Reverse Engineering Inspector",
        "about.body": (
            "The BylickiLabs Python Reverse Engineering Inspector is a business application "
            "for static inspection and structural decomposition of Python projects. It analyzes "
            "source code, modules, classes, functions, imports, dependencies, function calls, "
            "complexity and selected security-relevant patterns.\n\n"
            "NumPy calculates statistical project metrics including mean, median, standard "
            "deviation and percentiles. SciPy adds Z-score-based detection of unusual complexity "
            "values.\n\n"
            "The inspected project is not imported or executed. Analysis is based on the Python "
            "AST. The Bytecode view only compiles source code into code objects and disassembles "
            "them without execution.\n\n"
            "Core areas:\n"
            "• Project and symbol structure\n"
            "• Dependency analysis\n"
            "• Call graph analysis\n"
            "• Complexity metrics\n"
            "• Risk pattern analysis\n"
            "• NumPy/SciPy statistics\n"
            "• Bytecode inspection\n"
            "• SQLite history\n"
            "• JSON, CSV, HTML and Markdown export\n"
            "• Complete German and English interface\n\n"
            "Version: {version}\n"
            "Developer: {author}"
        ),
        "export.filter": "JSON (*.json);;CSV (*.csv);;HTML (*.html);;Markdown (*.md)",
    },
}


class Translator:
    def __init__(self, language: str = "de"):
        self.language = language if language in TRANSLATIONS else "de"

    def set_language(self, language: str) -> None:
        if language in TRANSLATIONS:
            self.language = language

    def t(self, key: str, **kwargs) -> str:
        value = TRANSLATIONS.get(self.language, {}).get(
            key,
            TRANSLATIONS["de"].get(key, key),
        )

        return value.format(**kwargs) if kwargs else value
