from abc import ABC, abstractmethod
from typing import List
from app.models.news_item import NewsItem


class BaseCrawler(ABC):
    """抽象爬虫类：所有新闻源爬虫都继承该类。"""

    def __init__(self, source_name: str):
        self.source_name = source_name

    @abstractmethod
    def crawl(self) -> List[NewsItem]:
        """采集新闻，返回统一 NewsItem 列表。"""
        raise NotImplementedError
