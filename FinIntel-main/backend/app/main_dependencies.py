from app.repositories.database import DatabaseManager
from app.repositories.news_repository import NewsRepository
from app.repositories.event_repository import EventRepository
from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.graph_repository import GraphRepository

db_manager = DatabaseManager()
news_repo = NewsRepository(db_manager)
event_repo = EventRepository(db_manager)
analysis_repo = AnalysisRepository(db_manager)
graph_repo = GraphRepository(db_manager)


def get_db_manager() -> DatabaseManager:
    return db_manager


def get_news_repo() -> NewsRepository:
    return news_repo


def get_event_repo() -> EventRepository:
    return event_repo


def get_analysis_repo() -> AnalysisRepository:
    return analysis_repo


def get_graph_repo() -> GraphRepository:
    return graph_repo
