from app.repositories.graph_repository import GraphRepository
from app.models.news_item import NewsItem
from app.models.analysis_result import AnalysisResult


class KnowledgeGraphService:
    """轻量级知识图谱构建服务：使用 SQLite 节点表和边表模拟图数据库。"""

    def __init__(self, graph_repo: GraphRepository):
        self.graph_repo = graph_repo

    def build_from_analysis(self, event_id: int, news: NewsItem, analysis: AnalysisResult) -> None:
        event_node_id = f"event_{event_id}"
        stock_node_id = f"stock_{news.stock_code}" if news.stock_code else "stock_unknown"
        industry_node_id = f"industry_{news.industry}" if news.industry else "industry_unknown"
        source_node_id = f"source_{news.source}"

        self.graph_repo.upsert_node(event_node_id, news.title, "event", {"event_type": analysis.event_type})
        self.graph_repo.upsert_node(stock_node_id, news.stock_name or news.stock_code or "未知股票", "stock", {"code": news.stock_code})
        self.graph_repo.upsert_node(industry_node_id, news.industry or "未知行业", "industry", {})
        self.graph_repo.upsert_node(source_node_id, news.source, "source", {})

        self.graph_repo.upsert_edge(event_node_id, stock_node_id, "影响", analysis.impact_score, {"direction": analysis.sentiment})
        self.graph_repo.upsert_edge(stock_node_id, industry_node_id, "属于", 1.0, {})
        self.graph_repo.upsert_edge(source_node_id, event_node_id, "报道", 1.0, {})
