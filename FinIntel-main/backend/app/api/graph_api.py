from fastapi import APIRouter, Depends
from app.repositories.graph_repository import GraphRepository
from app.main_dependencies import get_graph_repo

router = APIRouter(prefix="/api/graph", tags=["graph"])


@router.get("")
def get_graph(repo: GraphRepository = Depends(get_graph_repo)):
    return repo.get_graph()
