from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from src.config import DB_FILENAME
from src.models import AnalysisResult


class HistoryDatabase:
    def __init__(self):
        base = Path.home() / ".bprei"
        base.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.path = base / DB_FILENAME

        with self._connect() as con:
            con.execute(
                """
                CREATE TABLE IF NOT EXISTS analysis_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    analyzed_at TEXT NOT NULL,
                    project_name TEXT NOT NULL,
                    project_path TEXT NOT NULL,
                    summary_json TEXT NOT NULL
                )
                """
            )

    def _connect(self):
        return sqlite3.connect(self.path)

    def save(
        self,
        result: AnalysisResult,
    ):
        metrics = result.metrics

        summary = {
            "files": metrics.files,
            "classes": metrics.classes,
            "functions": metrics.functions,
            "methods": metrics.methods,
            "dependencies": metrics.dependencies,
            "risks": metrics.risk_findings,
            "average_complexity": metrics.average_complexity,
        }

        with self._connect() as con:
            con.execute(
                """
                INSERT INTO analysis_history (
                    analyzed_at,
                    project_name,
                    project_path,
                    summary_json
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    result.analyzed_at,
                    result.project_name,
                    result.project_path,
                    json.dumps(
                        summary,
                        ensure_ascii=False,
                    ),
                ),
            )

    def recent(
        self,
        limit: int = 100,
    ):
        with self._connect() as con:
            rows = con.execute(
                """
                SELECT
                    analyzed_at,
                    project_name,
                    project_path,
                    summary_json
                FROM analysis_history
                ORDER BY id DESC
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

        return [
            {
                "analyzed_at": row[0],
                "project_name": row[1],
                "project_path": row[2],
                "summary": json.loads(row[3]),
            }
            for row in rows
        ]