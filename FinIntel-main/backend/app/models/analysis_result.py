from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class AnalysisResult:
    """智能分析结果对象。"""
    event_id: int
    sentiment: str
    sentiment_score: float
    impact_score: float
    risk_score: float
    confidence_score: float
    related_stock_code: str
    related_stock_name: str
    related_industry: str
    analysis_reason: str
    summary: str
    event_type: str
    analysis_id: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)
