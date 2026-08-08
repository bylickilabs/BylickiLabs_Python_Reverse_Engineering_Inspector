from __future__ import annotations

import sys
import webbrowser
from pathlib import Path

from PySide6.QtCore import QThread, Qt, Signal
from PySide6.QtGui import QFontDatabase
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QFileDialog,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QSplitter,
    QTabWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from src.analyzers.bytecode_analyzer import disassemble_source
from src.analyzers.project_analyzer import ProjectAnalyzer
from src.config import (
    APP_AUTHOR,
    APP_NAME,
    APP_SHORT_NAME,
    APP_VERSION,
    FACEBOOK_URL,
    GITHUB_URL,
    LINKEDIN_URL,
)
from src.localization import Translator
from src.models import AnalysisResult, SymbolInfo
from src.services.database import HistoryDatabase
from src.services.exporter import export_result


STYLE = """
QMainWindow,
QWidget {
    background: #0f141a;
    color: #e7edf4;
    font-family: "Segoe UI";
    font-size: 10.5pt;
}

QFrame#header {
    background: #141b23;
    border-bottom: 1px solid #25303b;
}

QFrame#card {
    background: #151d26;
    border: 1px solid #273340;
    border-radius: 10px;
}

QFrame#headerSeparator {
    background: #3a4652;
    border: none;
    min-width: 1px;
    max-width: 1px;
    margin-top: 5px;
    margin-bottom: 5px;
}

QLabel#appTitle {
    font-size: 18pt;
    font-weight: 700;
    color: #ffffff;
}

QLabel#subtitle {
    color: #92a3b4;
}

QLabel#cardTitle {
    color: #91a2b3;
    font-size: 9pt;
}

QLabel#cardValue {
    color: #ffffff;
    font-size: 19pt;
    font-weight: 700;
}

QPushButton {
    background: #1c2631;
    border: 1px solid #31404f;
    border-radius: 7px;
    padding: 8px 12px;
    color: #edf3f8;
}

QPushButton:hover {
    background: #24313e;
}

QPushButton:pressed {
    background: #18212a;
}

QPushButton#primary {
    background: #17804d;
    border-color: #21995f;
    font-weight: 700;
}

QPushButton#primary:hover {
    background: #1d9560;
}

QPushButton:disabled {
    color: #677482;
    background: #161d24;
    border-color: #222c35;
}

QTabWidget::pane {
    border: 1px solid #273340;
    background: #111820;
}

QTabBar::tab {
    background: #151d26;
    color: #9dafbf;
    padding: 10px 14px;
    border: 1px solid #273340;
    border-bottom: none;
}

QTabBar::tab:selected {
    color: #ffffff;
    background: #1b2631;
}

QTreeWidget,
QTableWidget,
QPlainTextEdit,
QTextEdit {
    background: #111820;
    alternate-background-color: #141d26;
    border: 1px solid #273340;
    selection-background-color: #235b45;
    selection-color: #ffffff;
}

QHeaderView::section {
    background: #1a232d;
    color: #d9e3ec;
    border: none;
    border-right: 1px solid #2a3642;
    padding: 7px;
}

QProgressBar {
    border: 1px solid #2b3845;
    border-radius: 5px;
    background: #151c23;
    text-align: center;
}

QProgressBar::chunk {
    background: #23895a;
    border-radius: 4px;
}

QSplitter::handle {
    background: #27323d;
}
"""


class AnalysisThread(QThread):
    progress = Signal(int, str)
    completed = Signal(object)
    failed = Signal(str)
    cancelled = Signal()

    def __init__(self, path: str, parent=None):
        super().__init__(parent)
        self.path = path
        self._cancel_requested = False

    def cancel(self) -> None:
        self._cancel_requested = True

    def run(self) -> None:
        try:
            analyzer = ProjectAnalyzer(lambda: self._cancel_requested)
            result = analyzer.analyze(
                self.path,
                lambda progress, detail: self.progress.emit(progress, detail),
            )

            if self._cancel_requested:
                self.cancelled.emit()
            else:
                self.completed.emit(result)
        except InterruptedError:
            self.cancelled.emit()
        except Exception as exc:
            self.failed.emit(str(exc))


class MetricCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)

        self.title = QLabel()
        self.title.setObjectName("cardTitle")

        self.value = QLabel("0")
        self.value.setObjectName("cardValue")

        layout.addWidget(self.title)
        layout.addWidget(self.value)


class AboutDialog(QDialog):
    def __init__(self, translator: Translator, parent=None):
        super().__init__(parent)
        self.setMinimumSize(720, 600)
        self.setWindowTitle(translator.t("about.title"))

        layout = QVBoxLayout(self)

        heading = QLabel(translator.t("about.heading"))
        heading.setObjectName("appTitle")

        body = QTextEdit()
        body.setReadOnly(True)
        body.setPlainText(
            translator.t(
                "about.body",
                version=APP_VERSION,
                author=APP_AUTHOR,
            )
        )

        close_button = QPushButton(translator.t("button.close"))
        close_button.clicked.connect(self.accept)

        layout.addWidget(heading)
        layout.addWidget(body, 1)
        layout.addWidget(close_button, alignment=Qt.AlignRight)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tr = Translator("de")
        self.db = HistoryDatabase()

        self.project_path = ""
        self.result: AnalysisResult | None = None
        self.thread: AnalysisThread | None = None
        self.selected_file = ""

        self.setWindowTitle(f"{APP_NAME} {APP_VERSION}")
        self.resize(1540, 920)
        self.setMinimumSize(1180, 720)

        self._build_ui()
        self.setStyleSheet(STYLE)
        self._apply_translations()
        self._load_history()
        self._update_actions()

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------

    def _build_ui(self) -> None:
        central = QWidget()
        outer = QVBoxLayout(central)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        outer.addWidget(self._build_header())

        body = QVBoxLayout()
        body.setContentsMargins(14, 14, 14, 10)
        body.setSpacing(10)

        self.tabs = QTabWidget()
        self.dashboard_tab = QWidget()
        self.explorer_tab = QWidget()
        self.dependencies_tab = QWidget()
        self.calls_tab = QWidget()
        self.complexity_tab = QWidget()
        self.risks_tab = QWidget()
        self.bytecode_tab = QWidget()
        self.history_tab = QWidget()

        for tab in (
            self.dashboard_tab,
            self.explorer_tab,
            self.dependencies_tab,
            self.calls_tab,
            self.complexity_tab,
            self.risks_tab,
            self.bytecode_tab,
            self.history_tab,
        ):
            self.tabs.addTab(tab, "")

        self._build_dashboard_tab()
        self._build_explorer_tab()
        self.dep_table = self._build_table_tab(self.dependencies_tab, 4)
        self.call_table = self._build_table_tab(self.calls_tab, 4)
        self.complexity_table = self._build_table_tab(self.complexity_tab, 5)
        self.risk_table = self._build_table_tab(self.risks_tab, 6)
        self._build_bytecode_tab()
        self._build_history_tab()

        body.addWidget(self.tabs, 1)
        body.addLayout(self._build_status_bar())

        outer.addLayout(body, 1)
        self.setCentralWidget(central)

    def _build_header(self) -> QFrame:
        header = QFrame()
        header.setObjectName("header")

        layout = QHBoxLayout(header)
        layout.setContentsMargins(18, 14, 18, 14)
        layout.setSpacing(8)

        title_layout = QVBoxLayout()
        title_layout.setSpacing(2)

        self.title = QLabel(APP_NAME)
        self.title.setObjectName("appTitle")

        self.subtitle = QLabel()
        self.subtitle.setObjectName("subtitle")

        title_layout.addWidget(self.title)
        title_layout.addWidget(self.subtitle)

        layout.addLayout(title_layout)
        layout.addStretch(1)

        # Application actions
        self.open_btn = QPushButton()
        self.open_btn.clicked.connect(self.open_project)

        self.analyze_btn = QPushButton()
        self.analyze_btn.setObjectName("primary")
        self.analyze_btn.clicked.connect(self.start_analysis)

        self.cancel_btn = QPushButton()
        self.cancel_btn.clicked.connect(self.cancel_analysis)

        self.export_btn = QPushButton()
        self.export_btn.clicked.connect(self.export_report)

        # Social media
        self.github_btn = QPushButton("GitHub")
        self.github_btn.clicked.connect(lambda: self._open_url(GITHUB_URL))

        self.linkedin_btn = QPushButton("LinkedIn")
        self.linkedin_btn.clicked.connect(lambda: self._open_url(LINKEDIN_URL))

        self.facebook_btn = QPushButton("Facebook")
        self.facebook_btn.clicked.connect(lambda: self._open_url(FACEBOOK_URL))

        # Application information / language
        self.info_btn = QPushButton()
        self.info_btn.clicked.connect(self.show_about)

        self.lang_btn = QPushButton()
        self.lang_btn.clicked.connect(self.toggle_language)

        # Group 1: project/application actions
        layout.addWidget(self.open_btn)
        layout.addWidget(self.analyze_btn)
        layout.addWidget(self.cancel_btn)
        layout.addWidget(self.export_btn)

        # Separator: Export | Social Media
        layout.addSpacing(2)
        layout.addWidget(self._create_header_separator())
        layout.addSpacing(2)

        # Group 2: social media
        layout.addWidget(self.github_btn)
        layout.addWidget(self.linkedin_btn)
        layout.addWidget(self.facebook_btn)

        # Separator: Facebook | Info
        layout.addSpacing(2)
        layout.addWidget(self._create_header_separator())
        layout.addSpacing(2)

        # Group 3: info / language
        layout.addWidget(self.info_btn)
        layout.addWidget(self.lang_btn)

        return header

    @staticmethod
    def _create_header_separator() -> QFrame:
        separator = QFrame()
        separator.setObjectName("headerSeparator")
        separator.setFrameShape(QFrame.VLine)
        separator.setFrameShadow(QFrame.Plain)
        separator.setFixedWidth(1)
        separator.setMinimumHeight(30)
        return separator

    def _build_status_bar(self) -> QHBoxLayout:
        layout = QHBoxLayout()

        self.status_label = QLabel()

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setMaximumWidth(480)

        layout.addWidget(self.status_label, 1)
        layout.addWidget(self.progress)
        return layout

    def _build_dashboard_tab(self) -> None:
        layout = QVBoxLayout(self.dashboard_tab)

        self.dashboard_heading = QLabel()
        self.dashboard_heading.setObjectName("appTitle")
        layout.addWidget(self.dashboard_heading)

        grid = QGridLayout()
        self.cards = {
            key: MetricCard()
            for key in (
                "files",
                "classes",
                "functions",
                "dependencies",
                "code_lines",
                "risks",
                "avg_complexity",
                "max_complexity",
                "outliers",
            )
        }

        for index, key in enumerate(self.cards):
            grid.addWidget(self.cards[key], index // 3, index % 3)

        layout.addLayout(grid)

        self.anomaly_heading = QLabel()
        self.anomaly_heading.setObjectName("appTitle")
        layout.addWidget(self.anomaly_heading)

        self.anomaly_table = QTableWidget(0, 5)
        self._style_table(self.anomaly_table)
        layout.addWidget(self.anomaly_table, 1)

    def _build_explorer_tab(self) -> None:
        layout = QVBoxLayout(self.explorer_tab)
        splitter = QSplitter(Qt.Horizontal)

        left = QWidget()
        left_layout = QVBoxLayout(left)
        self.explorer_files_label = QLabel()
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemClicked.connect(self.on_tree_item)
        left_layout.addWidget(self.explorer_files_label)
        left_layout.addWidget(self.tree, 1)

        center = QWidget()
        center_layout = QVBoxLayout(center)
        self.source_label = QLabel()
        self.code = QPlainTextEdit()
        self.code.setReadOnly(True)
        self.code.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont))
        center_layout.addWidget(self.source_label)
        center_layout.addWidget(self.code, 1)

        right = QWidget()
        right_layout = QVBoxLayout(right)
        self.details_label = QLabel()
        self.details = QTextEdit()
        self.details.setReadOnly(True)
        right_layout.addWidget(self.details_label)
        right_layout.addWidget(self.details, 1)

        splitter.addWidget(left)
        splitter.addWidget(center)
        splitter.addWidget(right)
        splitter.setSizes([320, 760, 360])

        layout.addWidget(splitter)

    def _build_table_tab(self, tab: QWidget, columns: int) -> QTableWidget:
        layout = QVBoxLayout(tab)
        table = QTableWidget(0, columns)
        self._style_table(table)
        layout.addWidget(table)
        return table

    def _build_bytecode_tab(self) -> None:
        layout = QVBoxLayout(self.bytecode_tab)

        self.bytecode_help = QLabel()
        self.bytecode_help.setWordWrap(True)

        self.bytecode = QPlainTextEdit()
        self.bytecode.setReadOnly(True)
        self.bytecode.setFont(QFontDatabase.systemFont(QFontDatabase.FixedFont))

        layout.addWidget(self.bytecode_help)
        layout.addWidget(self.bytecode, 1)

    def _build_history_tab(self) -> None:
        layout = QVBoxLayout(self.history_tab)

        controls = QHBoxLayout()
        controls.addStretch(1)

        self.refresh_btn = QPushButton()
        self.refresh_btn.clicked.connect(self._load_history)
        controls.addWidget(self.refresh_btn)

        self.history_table = QTableWidget(0, 4)
        self._style_table(self.history_table)

        layout.addLayout(controls)
        layout.addWidget(self.history_table)

    @staticmethod
    def _style_table(table: QTableWidget) -> None:
        table.setAlternatingRowColors(True)
        table.setSortingEnabled(True)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    @staticmethod
    def _set_headers(table: QTableWidget, labels: list[str]) -> None:
        table.setHorizontalHeaderLabels(labels)

    # ------------------------------------------------------------------
    # Localization
    # ------------------------------------------------------------------

    def _apply_translations(self) -> None:
        t = self.tr.t

        self.subtitle.setText(t("app.subtitle"))

        self.open_btn.setText(t("button.open_project"))
        self.analyze_btn.setText(t("button.analyze"))
        self.cancel_btn.setText(t("button.cancel"))
        self.export_btn.setText(t("button.export"))
        self.info_btn.setText(t("button.info"))
        self.lang_btn.setText(t("button.language"))
        self.refresh_btn.setText(t("button.refresh"))

        tab_keys = (
            "nav.dashboard",
            "nav.explorer",
            "nav.dependencies",
            "nav.calls",
            "nav.complexity",
            "nav.risks",
            "nav.bytecode",
            "nav.history",
        )
        for index, key in enumerate(tab_keys):
            self.tabs.setTabText(index, t(key))

        self.dashboard_heading.setText(t("dashboard.overview"))
        self.anomaly_heading.setText(t("dashboard.anomalies"))
        self.explorer_files_label.setText(t("explorer.files"))
        self.source_label.setText(t("explorer.source"))
        self.details_label.setText(t("explorer.details"))
        self.bytecode_help.setText(t("bytecode.help"))

        card_keys = {
            "files": "dashboard.files",
            "classes": "dashboard.classes",
            "functions": "dashboard.functions",
            "dependencies": "dashboard.dependencies",
            "code_lines": "dashboard.code_lines",
            "risks": "dashboard.risks",
            "avg_complexity": "dashboard.avg_complexity",
            "max_complexity": "dashboard.max_complexity",
            "outliers": "dashboard.outliers",
        }
        for card_name, translation_key in card_keys.items():
            self.cards[card_name].title.setText(t(translation_key))

        self._set_headers(
            self.anomaly_table,
            [
                t("table.symbol"),
                t("table.file"),
                t("table.line"),
                t("table.complexity"),
                t("table.zscore"),
            ],
        )
        self._set_headers(
            self.dep_table,
            [
                t("table.module"),
                t("table.type"),
                t("table.uses"),
                t("table.file"),
            ],
        )
        self._set_headers(
            self.call_table,
            [
                t("table.caller"),
                t("table.callee"),
                t("table.file"),
                t("table.line"),
            ],
        )
        self._set_headers(
            self.complexity_table,
            [
                t("table.symbol"),
                t("table.type"),
                t("table.file"),
                t("table.line"),
                t("table.complexity"),
            ],
        )
        self._set_headers(
            self.risk_table,
            [
                t("table.severity"),
                t("table.finding"),
                t("table.file"),
                t("table.line"),
                t("table.symbol"),
                t("table.evidence"),
            ],
        )
        self._set_headers(
            self.history_table,
            [
                t("table.date"),
                t("table.project"),
                t("table.path"),
                t("table.summary"),
            ],
        )

        if self.thread is None:
            self.status_label.setText(
                t("status.done") if self.result is not None else t("status.ready")
            )

        if self.result is not None:
            self._populate_all()

        self._load_history()

    def toggle_language(self) -> None:
        self.tr.set_language("en" if self.tr.language == "de" else "de")
        self._apply_translations()

    # ------------------------------------------------------------------
    # Project / analysis lifecycle
    # ------------------------------------------------------------------

    def open_project(self) -> None:
        folder = QFileDialog.getExistingDirectory(
            self,
            self.tr.t("dialog.select_project"),
            self.project_path or str(Path.home()),
        )
        if not folder:
            return

        self.project_path = folder
        self.status_label.setText(folder)
        self._update_actions()

    def start_analysis(self) -> None:
        if not self.project_path:
            QMessageBox.information(
                self,
                APP_SHORT_NAME,
                self.tr.t("dialog.no_project"),
            )
            return

        self.result = None
        self._clear_views()

        self.thread = AnalysisThread(self.project_path, self)
        self.thread.progress.connect(self.on_progress)
        self.thread.completed.connect(self.on_done)
        self.thread.failed.connect(self.on_failed)
        self.thread.cancelled.connect(self.on_cancelled)
        self.thread.finished.connect(self._on_thread_finished)

        self.status_label.setText(self.tr.t("status.loading"))
        self.progress.setValue(0)
        self._update_actions()
        self.thread.start()

    def cancel_analysis(self) -> None:
        if self.thread is not None:
            self.thread.cancel()
            self.cancel_btn.setEnabled(False)

    def on_progress(self, value: int, detail: str) -> None:
        self.progress.setValue(value)

        suffix = ""
        if detail not in {"metrics", "done"}:
            suffix = f"  {detail}"

        self.status_label.setText(self.tr.t("status.loading") + suffix)

    def on_done(self, result: AnalysisResult) -> None:
        self.result = result

        try:
            self.db.save(result)
        except Exception:
            pass

        self.progress.setValue(100)
        self.status_label.setText(self.tr.t("status.done"))
        self._populate_all()
        self._load_history()

    def on_failed(self, message: str) -> None:
        self.progress.setValue(0)
        self.status_label.setText(self.tr.t("status.failed"))

        display_message = (
            self.tr.t("dialog.project_invalid")
            if message == "NO_PYTHON_FILES"
            else message
        )

        QMessageBox.critical(
            self,
            self.tr.t("dialog.error"),
            display_message,
        )

    def on_cancelled(self) -> None:
        self.progress.setValue(0)
        self.status_label.setText(self.tr.t("status.cancelled"))

    def _on_thread_finished(self) -> None:
        finished_thread = self.thread
        self.thread = None

        if finished_thread is not None:
            finished_thread.deleteLater()

        self._update_actions()

    def _update_actions(self) -> None:
        running = self.thread is not None

        self.open_btn.setEnabled(not running)
        self.analyze_btn.setEnabled(bool(self.project_path) and not running)
        self.cancel_btn.setEnabled(running)
        self.export_btn.setEnabled(self.result is not None and not running)
        self.lang_btn.setEnabled(not running)

    # ------------------------------------------------------------------
    # View population
    # ------------------------------------------------------------------

    def _clear_views(self) -> None:
        self.tree.clear()
        self.code.clear()
        self.details.clear()
        self.bytecode.clear()

        for table in (
            self.dep_table,
            self.call_table,
            self.complexity_table,
            self.risk_table,
            self.anomaly_table,
        ):
            table.setRowCount(0)

        for card in self.cards.values():
            card.value.setText("0")

    def _populate_all(self) -> None:
        if self.result is None:
            return

        self._populate_dashboard()
        self._populate_tree()
        self._populate_dependencies()
        self._populate_calls()
        self._populate_complexity()
        self._populate_risks()

    def _populate_dashboard(self) -> None:
        if self.result is None:
            return

        metrics = self.result.metrics
        code_lines = (
            f"{metrics.code_lines:,}".replace(",", ".")
            if self.tr.language == "de"
            else f"{metrics.code_lines:,}"
        )

        values = {
            "files": metrics.files,
            "classes": metrics.classes,
            "functions": metrics.functions + metrics.methods,
            "dependencies": metrics.dependencies,
            "code_lines": code_lines,
            "risks": metrics.risk_findings,
            "avg_complexity": f"{metrics.average_complexity:.2f}",
            "max_complexity": metrics.max_complexity,
            "outliers": metrics.complexity_outliers,
        }

        for key, value in values.items():
            self.cards[key].value.setText(str(value))

        self.anomaly_table.setSortingEnabled(False)
        self.anomaly_table.setRowCount(len(self.result.anomalies))

        for row, anomaly in enumerate(self.result.anomalies):
            values = (
                anomaly.symbol,
                anomaly.file,
                anomaly.line,
                anomaly.complexity,
                f"{anomaly.z_score:.2f}",
            )
            for column, value in enumerate(values):
                self.anomaly_table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value)),
                )

        self.anomaly_table.setSortingEnabled(True)

    def _populate_tree(self) -> None:
        if self.result is None:
            return

        self.tree.clear()

        root = QTreeWidgetItem([self.result.project_name])
        root.setData(0, Qt.UserRole, {"type": "root"})
        self.tree.addTopLevelItem(root)

        folders: dict[str, QTreeWidgetItem] = {"": root}

        for file_analysis in self.result.python_files:
            parts = file_analysis.relative_path.split("/")
            parent = root
            prefix = ""

            for part in parts[:-1]:
                prefix = f"{prefix}/{part}".strip("/")
                if prefix not in folders:
                    folder_item = QTreeWidgetItem([part])
                    folder_item.setData(0, Qt.UserRole, {"type": "folder"})
                    parent.addChild(folder_item)
                    folders[prefix] = folder_item
                parent = folders[prefix]

            file_item = QTreeWidgetItem([parts[-1]])
            file_item.setData(
                0,
                Qt.UserRole,
                {
                    "type": "file",
                    "file": file_analysis.relative_path,
                },
            )
            parent.addChild(file_item)

            for symbol in file_analysis.symbols:
                symbol_item = QTreeWidgetItem(
                    [f"{self.tr.t('kind.' + symbol.kind)}: {symbol.name}"]
                )
                symbol_item.setData(
                    0,
                    Qt.UserRole,
                    {
                        "type": "symbol",
                        "file": file_analysis.relative_path,
                        "symbol": symbol,
                    },
                )
                file_item.addChild(symbol_item)

        root.setExpanded(True)

    def _populate_dependencies(self) -> None:
        if self.result is None:
            return

        self.dep_table.setSortingEnabled(False)
        self.dep_table.setRowCount(len(self.result.dependencies))

        for row, (name, info) in enumerate(self.result.dependencies.items()):
            values = (
                name,
                self.tr.t("dep." + info["category"]),
                info["uses"],
                ", ".join(info["files"]),
            )
            for column, value in enumerate(values):
                self.dep_table.setItem(row, column, QTableWidgetItem(str(value)))

        self.dep_table.setSortingEnabled(True)

    def _populate_calls(self) -> None:
        if self.result is None:
            return

        calls = [
            call
            for file_analysis in self.result.python_files
            for call in file_analysis.calls
        ]

        self.call_table.setSortingEnabled(False)
        self.call_table.setRowCount(len(calls))

        for row, call in enumerate(calls):
            values = (call.caller, call.callee, call.file, call.line)
            for column, value in enumerate(values):
                self.call_table.setItem(row, column, QTableWidgetItem(str(value)))

        self.call_table.setSortingEnabled(True)

    def _populate_complexity(self) -> None:
        if self.result is None:
            return

        symbols = [
            symbol
            for file_analysis in self.result.python_files
            for symbol in file_analysis.symbols
            if symbol.kind
            in {"function", "async_function", "method", "async_method"}
        ]

        self.complexity_table.setSortingEnabled(False)
        self.complexity_table.setRowCount(len(symbols))

        for row, symbol in enumerate(symbols):
            full_name = (
                f"{symbol.parent}.{symbol.name}"
                if symbol.parent
                else symbol.name
            )
            values = (
                full_name,
                self.tr.t("kind." + symbol.kind),
                symbol.file,
                symbol.line,
                symbol.complexity,
            )
            for column, value in enumerate(values):
                self.complexity_table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value)),
                )

        self.complexity_table.setSortingEnabled(True)

    def _populate_risks(self) -> None:
        if self.result is None:
            return

        risks = [
            risk
            for file_analysis in self.result.python_files
            for risk in file_analysis.risks
        ]

        self.risk_table.setSortingEnabled(False)
        self.risk_table.setRowCount(len(risks))

        for row, risk in enumerate(risks):
            values = (
                self.tr.t("severity." + risk.severity),
                self.tr.t("risk." + risk.code),
                risk.file,
                risk.line,
                risk.symbol,
                risk.evidence,
            )
            for column, value in enumerate(values):
                self.risk_table.setItem(row, column, QTableWidgetItem(str(value)))

        self.risk_table.setSortingEnabled(True)

    # ------------------------------------------------------------------
    # Project explorer / bytecode
    # ------------------------------------------------------------------

    def on_tree_item(self, item: QTreeWidgetItem, column: int) -> None:
        del column

        data = item.data(0, Qt.UserRole) or {}
        item_type = data.get("type")

        if item_type not in {"file", "symbol"} or self.result is None:
            return

        file_analysis = next(
            (
                file_analysis
                for file_analysis in self.result.python_files
                if file_analysis.relative_path == data["file"]
            ),
            None,
        )
        if file_analysis is None:
            return

        try:
            source = Path(file_analysis.absolute_path).read_text(
                encoding="utf-8",
                errors="replace",
            )
        except OSError as exc:
            QMessageBox.critical(
                self,
                self.tr.t("dialog.error"),
                str(exc),
            )
            return

        self.selected_file = file_analysis.relative_path
        self.code.setPlainText(source)
        self._show_bytecode(source, file_analysis.absolute_path)

        if item_type == "symbol":
            symbol: SymbolInfo = data["symbol"]
            self._show_symbol(symbol)
            self._jump_to_line(symbol.line)
            return

        details = (
            f"{file_analysis.relative_path}\n\n"
            + self.tr.t(
                "explorer.file_stats",
                lines=file_analysis.lines,
                symbols=len(file_analysis.symbols),
                imports=len(file_analysis.imports),
            )
        )

        if file_analysis.syntax_error:
            details += "\n\n" + self.tr.t(
                "explorer.syntax",
                error=file_analysis.syntax_error,
            )

        self.details.setPlainText(details)

    def _show_symbol(self, symbol: SymbolInfo) -> None:
        t = self.tr.t

        lines = [
            f"{t('detail.kind')}: {t('kind.' + symbol.kind)}",
            f"{t('detail.file')}: {symbol.file}",
            f"{t('detail.line')}: {symbol.line}",
            f"{t('detail.lines')}: {symbol.line}-{symbol.end_line}",
            f"{t('detail.complexity')}: {symbol.complexity}",
            "",
            f"{t('detail.parameters')}: {', '.join(symbol.parameters) or '-'}",
            f"{t('detail.decorators')}: {', '.join(symbol.decorators) or '-'}",
            "",
            f"{t('detail.calls')}:",
        ]

        if symbol.calls:
            lines.extend(f"  • {call}" for call in symbol.calls)
        else:
            lines.append("  -")

        self.details.setPlainText("\n".join(lines))

    def _jump_to_line(self, line_number: int) -> None:
        cursor = self.code.textCursor()
        block = self.code.document().findBlockByLineNumber(max(0, line_number - 1))
        cursor.setPosition(block.position())
        self.code.setTextCursor(cursor)
        self.code.centerCursor()

    def _show_bytecode(self, source: str, filename: str) -> None:
        try:
            self.bytecode.setPlainText(disassemble_source(source, filename))
        except Exception as exc:
            self.bytecode.setPlainText(
                f"{self.tr.t('bytecode.error')}\n\n{exc}"
            )

    # ------------------------------------------------------------------
    # Export / history / external links
    # ------------------------------------------------------------------

    def export_report(self) -> None:
        if self.result is None:
            QMessageBox.information(
                self,
                APP_SHORT_NAME,
                self.tr.t("dialog.no_result"),
            )
            return

        default_filename = f"{self.result.project_name}_BPREI_Report.json"
        path, selected_filter = QFileDialog.getSaveFileName(
            self,
            self.tr.t("dialog.select_export"),
            default_filename,
            self.tr.t("export.filter"),
        )

        if not path:
            return

        if not Path(path).suffix:
            if "CSV" in selected_filter:
                path += ".csv"
            elif "HTML" in selected_filter:
                path += ".html"
            elif "Markdown" in selected_filter:
                path += ".md"
            else:
                path += ".json"

        try:
            export_result(self.result, path, self.tr.language)
            QMessageBox.information(
                self,
                self.tr.t("dialog.success"),
                self.tr.t("dialog.export_done"),
            )
        except Exception as exc:
            QMessageBox.critical(
                self,
                self.tr.t("dialog.error"),
                str(exc),
            )

    def _load_history(self) -> None:
        try:
            rows = self.db.recent()
        except Exception:
            rows = []

        self.history_table.setSortingEnabled(False)
        self.history_table.setRowCount(len(rows))

        for row, entry in enumerate(rows):
            summary_data = entry["summary"]
            summary = self.tr.t(
                "history.summary",
                files=summary_data.get("files", 0),
                deps=summary_data.get("dependencies", 0),
                risks=summary_data.get("risks", 0),
                complexity=summary_data.get("average_complexity", 0),
            )

            values = (
                entry["analyzed_at"],
                entry["project_name"],
                entry["project_path"],
                summary,
            )

            for column, value in enumerate(values):
                self.history_table.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value)),
                )

        self.history_table.setSortingEnabled(True)

    def show_about(self) -> None:
        dialog = AboutDialog(self.tr, self)
        dialog.setStyleSheet(STYLE)
        dialog.exec()

    @staticmethod
    def _open_url(url: str) -> None:
        webbrowser.open(url)


def run() -> None:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName("BylickiLabs")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
