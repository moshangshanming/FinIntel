class ImpactScorer:
    """影响评分器：课程提交版采用关键词规则。"""

    POSITIVE_KEYWORDS = ["增长", "订单", "中标", "回购", "增持", "利好", "突破", "上涨", "扩产", "合作", "盈利"]
    NEGATIVE_KEYWORDS = ["亏损", "处罚", "减持", "下跌", "风险", "调查", "退市", "违约", "暴雷", "监管"]

    def score(self, text: str) -> float:
        text = text or ""
        pos = sum(1 for word in self.POSITIVE_KEYWORDS if word in text)
        neg = sum(1 for word in self.NEGATIVE_KEYWORDS if word in text)
        base = 5.0 + pos * 1.2 - neg * 1.0
        return max(0.0, min(10.0, round(base, 2)))
