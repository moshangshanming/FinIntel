from dataclasses import dataclass, asdict


@dataclass
class StockRelation:
    """事件与股票之间的关联关系。"""
    event_id: int
    stock_code: str
    stock_name: str
    relation_type: str
    relation_strength: float
    impact_direction: str

    def to_dict(self) -> dict:
        return asdict(self)
