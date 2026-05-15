from typing import List
from app.crawlers.base_crawler import BaseCrawler
from app.models.news_item import NewsItem


class EastMoneyCrawler(BaseCrawler):
    """东方财富爬虫预留类。"""

    def __init__(self):
        super().__init__("东方财富")

    def crawl(self) -> List[NewsItem]:
        return []
