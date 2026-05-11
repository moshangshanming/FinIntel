from typing import List, Dict, Any
from sqlite3 import IntegrityError
from app.models.news_item import NewsItem
from app.repositories.database import DatabaseManager


class NewsRepository:
    """新闻表操作类。"""

    def __init__(self, db: DatabaseManager):
        self.db = db

    def insert_news(self, news: NewsItem) -> None:
        sql = """
        INSERT OR IGNORE INTO news_raw
        (title, content, source, publish_time, url, stock_code, stock_name, industry)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        with self.db.connect() as conn:
            conn.execute(sql, (
                news.title, news.content, news.source, news.publish_time, news.url,
                news.stock_code, news.stock_name, news.industry
            ))
            conn.commit()

    def list_news(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self.db.connect() as conn:
            rows = conn.execute("""
                SELECT * FROM news_raw
                ORDER BY publish_time DESC, id DESC
                LIMIT ?
            """, (limit,)).fetchall()
            return [dict(row) for row in rows]

    def count(self) -> int:
        with self.db.connect() as conn:
            return conn.execute("SELECT COUNT(*) AS c FROM news_raw").fetchone()["c"]
