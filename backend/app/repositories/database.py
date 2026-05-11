import sqlite3
from pathlib import Path
from app.config import DB_PATH, DATA_DIR


class DatabaseManager:
    """SQLite 数据库管理器。"""

    def __init__(self, db_path: Path = DB_PATH):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.db_path = db_path

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        with self.connect() as conn:
            cursor = conn.cursor()

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS news_raw (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT,
                source TEXT,
                publish_time TEXT,
                url TEXT UNIQUE,
                stock_code TEXT,
                stock_name TEXT,
                industry TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_title TEXT NOT NULL,
                event_summary TEXT,
                first_source TEXT,
                first_publish_time TEXT,
                event_type TEXT,
                duplicate_count INTEGER DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS analysis_results (
                analysis_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_id INTEGER,
                sentiment TEXT,
                sentiment_score REAL,
                impact_score REAL,
                risk_score REAL,
                confidence_score REAL,
                related_stock_code TEXT,
                related_stock_name TEXT,
                related_industry TEXT,
                analysis_reason TEXT,
                summary TEXT,
                event_type TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS kg_nodes (
                node_id TEXT PRIMARY KEY,
                name TEXT,
                node_type TEXT,
                properties TEXT
            )
            """)

            cursor.execute("""
            CREATE TABLE IF NOT EXISTS kg_edges (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id TEXT,
                target_id TEXT,
                relation_type TEXT,
                weight REAL,
                properties TEXT,
                UNIQUE(source_id, target_id, relation_type)
            )
            """)

            conn.commit()

    def clear_all(self) -> None:
        with self.connect() as conn:
            for table in ["news_raw", "events", "analysis_results", "kg_edges", "kg_nodes"]:
                conn.execute(f"DELETE FROM {table}")
            conn.commit()
