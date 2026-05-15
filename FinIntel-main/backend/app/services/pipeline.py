from typing import Dict, Any

from app.config import MOCK_NEWS_PATH
from app.crawlers.crawler_manager import CrawlerManager
from app.crawlers.mock_crawler import MockNewsCrawler
from app.repositories.news_repository import NewsRepository
from app.repositories.event_repository import EventRepository
from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.graph_repository import GraphRepository
from app.services.news_cleaner import NewsCleaner
from app.services.deduplicator import DeduplicationService
from app.services.llm_analyzer import LLMAnalyzer
from app.services.graph_builder import KnowledgeGraphService


class IntelligencePipeline:
    """金融情报处理总流程：采集 → 清洗 → 去重 → 分析 → 入库 → 图谱构建。"""

    def __init__(
        self,
        news_repo: NewsRepository,
        event_repo: EventRepository,
        analysis_repo: AnalysisRepository,
        graph_repo: GraphRepository,
    ):
        self.news_repo = news_repo
        self.event_repo = event_repo
        self.analysis_repo = analysis_repo
        self.graph_repo = graph_repo

        self.crawler_manager = CrawlerManager()
        self.crawler_manager.register(MockNewsCrawler(MOCK_NEWS_PATH))

        self.cleaner = NewsCleaner()
        self.deduplicator = DeduplicationService()
        self.analyzer = LLMAnalyzer()
        self.graph_service = KnowledgeGraphService(graph_repo)

    def run_once(self) -> Dict[str, Any]:
        raw_news = self.crawler_manager.crawl_all()
        cleaned_news = [self.cleaner.clean(item) for item in raw_news]
        unique_news, duplicate_map = self.deduplicator.deduplicate(cleaned_news)

        raw_count = 0
        event_count = 0
        analysis_count = 0

        for news in cleaned_news:
            self.news_repo.insert_news(news)
            raw_count += 1

        for news in unique_news:
            duplicate_count = duplicate_map.get(news.title, 1)
            event_id = self.event_repo.insert_event_from_news(news, duplicate_count)
            analysis = self.analyzer.analyze(event_id, news, duplicate_count)
            self.analysis_repo.insert_analysis(analysis)
            self.graph_service.build_from_analysis(event_id, news, analysis)
            event_count += 1
            analysis_count += 1

        return {
            "raw_news_count": raw_count,
            "unique_event_count": event_count,
            "analysis_count": analysis_count,
            "duplicate_count": max(0, raw_count - event_count),
            "crawler_status": self.crawler_manager.get_status(),
        }
