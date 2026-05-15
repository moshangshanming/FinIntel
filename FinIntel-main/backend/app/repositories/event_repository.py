from typing import List, Dict, Any
from app.models.news_item import NewsItem
from app.repositories.database import DatabaseManager


class EventRepository:
    """事件表操作类。"""

    def __init__(self, db: DatabaseManager):
        self.db = db

    def insert_event_from_news(self, news: NewsItem, duplicate_count: int = 1) -> int:
        summary = news.content[:120] if news.content else news.title
        with self.db.connect() as conn:
            cursor = conn.execute("""
                INSERT INTO events
                (event_title, event_summary, first_source, first_publish_time, event_type, duplicate_count)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (news.title, summary, news.source, news.publish_time, "待分析", duplicate_count))
            conn.commit()
            return cursor.lastrowid

    def list_events(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self.db.connect() as conn:
            rows = conn.execute("""
                SELECT * FROM events
                ORDER BY first_publish_time DESC, event_id DESC
                LIMIT ?
            """, (limit,)).fetchall()
            return [dict(row) for row in rows]

    def count(self) -> int:
        with self.db.connect() as conn:
            return conn.execute("SELECT COUNT(*) AS c FROM events").fetchone()["c"]