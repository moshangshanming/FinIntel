import json
from typing import List
from pathlib import Path
from app.crawlers.base_crawler import BaseCrawler
from app.models.news_item import NewsItem


class MockNewsCrawler(BaseCrawler):
    """模拟新闻采集器：课程提交版本优先使用本地 JSON，保证系统稳定运行。"""

    def __init__(self, data_path: Path):
        super().__init__("模拟财经新闻源")
        self.data_path = data_path

    def crawl(self) -> List[NewsItem]:
        if not self.data_path.exists():
            return []
        raw_items = json.loads(self.data_path.read_text(encoding="utf-8"))
        return [NewsItem(**item) for item in raw_items]
