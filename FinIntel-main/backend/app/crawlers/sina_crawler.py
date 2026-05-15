from typing import List
from app.crawlers.base_crawler import BaseCrawler
from app.models.news_item import NewsItem


class SinaCrawler(BaseCrawler):
    """新浪财经爬虫预留类：后续可接入真实网页解析。"""

    def __init__(self):
        super().__init__("新浪财经")

    def crawl(self) -> List[NewsItem]:
        # 课程提交版不强依赖真实网络，避免反爬和网络波动。
        return []
