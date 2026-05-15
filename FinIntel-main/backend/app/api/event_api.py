from fastapi import APIRouter, Depends
from app.repositories.event_repository import EventRepository
from app.main_dependencies import get_event_repo

router = APIRouter(prefix="/api/events", tags=["events"])


@router.get("")
def list_events(limit: int = 100, repo: EventRepository = Depends(get_event_repo)):
    return repo.list_events(limit)
