from fastapi import APIRouter, Depends
from app.repositories.news_repository import NewsRepository
from app.main_dependencies import get_news_repo

router = APIRouter(prefix="/api/news", tags=["news"])


@router.get("")
def list_news(limit: int = 100, repo: NewsRepository = Depends(get_news_repo)):
    return repo.list_news(limit)
