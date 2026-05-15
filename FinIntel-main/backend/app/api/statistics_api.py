from fastapi import APIRouter, Depends
from app.repositories.analysis_repository import AnalysisRepository
from app.repositories.news_repository import NewsRepository
from app.repositories.event_repository import EventRepository
from app.main_dependencies import get_analysis_repo, get_news_repo, get_event_repo

router = APIRouter(prefix="/api/statistics", tags=["statistics"])


@router.get("")
def get_statistics(
    analysis_repo: AnalysisRepository = Depends(get_analysis_repo),
    news_repo: NewsRepository = Depends(get_news_repo),
    event_repo: EventRepository = Depends(get_event_repo),
):
    stats = analysis_repo.statistics()
    stats["overview"] = {
        "news_count": news_repo.count(),
        "event_count": event_repo.count()
    }
    return stats
