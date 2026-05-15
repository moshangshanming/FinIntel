from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class EventItem:
    """事件对象：多条相似新闻去重融合后形成一个事件。"""
    event_title: str
    event_summary: str
    first_source: str
    first_publish_time: str
    event_type: str
    duplicate_count: int = 1
    event_id: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)
