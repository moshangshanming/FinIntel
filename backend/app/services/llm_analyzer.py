from app.models.news_item import NewsItem
from app.models.analysis_result import AnalysisResult
from app.services.impact_scorer import ImpactScorer
from app.services.risk_scorer import RiskScorer


class LLMAnalyzer:
    """
    智能分析器。
    课程提交版使用规则模拟 LLM 分析流程；后续可替换为真实大语言模型 API。
    """

    def __init__(self):
        self.impact_scorer = ImpactScorer()
        self.risk_scorer = RiskScorer()

    def _event_type(self, text: str) -> str:
        if any(k in text for k in ["政策", "监管", "证监会", "交易所"]):
            return "政策/监管"
        if any(k in text for k in ["订单", "中标", "合同", "合作"]):
            return "订单/合作"
        if any(k in text for k in ["业绩", "盈利", "亏损", "营收"]):
            return "业绩变化"
        if any(k in text for k in ["回购", "增持", "减持"]):
            return "资本运作"
        return "行业动态"

    def analyze(self, event_id: int, news: NewsItem, duplicate_count: int = 1) -> AnalysisResult:
        text = f"{news.title} {news.content}"
        impact_score = self.impact_scorer.score(text)
        risk_score = self.risk_scorer.score(text)

        if impact_score >= 6.5 and risk_score < 5:
            sentiment = "positive"
            sentiment_score = round(min(5.0, (impact_score - 5) * 0.9), 2)
            direction = "利好"
        elif risk_score >= 5:
            sentiment = "negative"
            sentiment_score = round(max(-5.0, -risk_score * 0.7), 2)
            direction = "利空"
        else:
            sentiment = "neutral"
            sentiment_score = 0.0
            direction = "中性"

        event_type = self._event_type(text)
        reason = (
            f"系统识别该事件类型为【{event_type}】，关联股票为 {news.stock_name or '未知'}，"
            f"所属行业为 {news.industry or '未知'}。根据关键词和风险特征，判断短期影响方向为{direction}。"
        )
        summary = (
            f"{news.title}。该事件被 {duplicate_count} 条新闻提及，"
            f"综合影响分为 {impact_score}，风险分为 {risk_score}。"
        )

        return AnalysisResult(
            event_id=event_id,
            sentiment=sentiment,
            sentiment_score=sentiment_score,
            impact_score=impact_score,
            risk_score=risk_score,
            confidence_score=round(0.72 + min(duplicate_count, 5) * 0.04, 2),
            related_stock_code=news.stock_code or "",
            related_stock_name=news.stock_name or "",
            related_industry=news.industry or "",
            analysis_reason=reason,
            summary=summary,
            event_type=event_type
        )
