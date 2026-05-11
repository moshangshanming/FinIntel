from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class NewsItem:
    """新闻对象：用于统一不同新闻源采集结果。"""
    title: str
    content: str
    source: str
    publish_time: str
    url: str
    stock_code: Optional[str] = ""
    stock_name: Optional[str] = ""
    industry: Optional[str] = ""

    def to_dict(self) -> dict:
        return asdict(self)
