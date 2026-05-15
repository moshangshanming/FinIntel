from fastapi import APIRouter, Depends
from app.repositories.analysis_repository import AnalysisRepository
from app.main_dependencies import get_analysis_repo

router = APIRouter(prefix="/api/analysis", tags=["analysis"])


@router.get("")
def list_analysis(limit: int = 100, repo: AnalysisRepository = Depends(get_analysis_repo)):
    return repo.list_analysis(limit)
