class RiskScorer:
    """风险评分器：根据负面关键词评估风险水平。"""

    RISK_KEYWORDS = ["处罚", "调查", "亏损", "减持", "退市", "违约", "诉讼", "监管", "债务", "风险"]

    def score(self, text: str) -> float:
        text = text or ""
        count = sum(1 for word in self.RISK_KEYWORDS if word in text)
        return max(0.0, min(10.0, round(1.5 + count * 1.6, 2)))
