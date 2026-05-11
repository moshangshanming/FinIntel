from typing import List
from app.models.news_item import NewsItem
from app.crawlers.base_crawler import BaseCrawler


class CrawlerManager:
    """多源采集调度器。"""

    def __init__(self):
        self.crawlers: List[BaseCrawler] = []

    def register(self, crawler: BaseCrawler) -> None:
        self.crawlers.append(crawler)

    def crawl_all(self) -> List[NewsItem]:
        result: List[NewsItem] = []
        for crawler in self.crawlers:
            result.extend(crawler.crawl())
        return result

    def get_status(self) -> list:
        return [
            {
                "source": crawler.source_name,
                "status": "ready"
            }
            for crawler in self.crawlers
        ]
