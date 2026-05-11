from typing import List
from app.crawlers.base_crawler import BaseCrawler
from app.models.news_item import NewsItem


class CLSCrawler(BaseCrawler):
    """财联社爬虫预留类。"""

    def __init__(self):
        super().__init__("财联社")

    def crawl(self) -> List[NewsItem]:
        return []
