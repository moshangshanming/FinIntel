from typing import List
from app.crawlers.base_crawler import BaseCrawler
from app.models.news_item import NewsItem


class THSCrawler(BaseCrawler):
    """同花顺爬虫预留类。"""

    def __init__(self):
        super().__init__("同花顺")

    def crawl(self) -> List[NewsItem]:
        return []
