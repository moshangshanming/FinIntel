from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import APP_NAME, APP_VERSION
from app.main_dependencies import db_manager, news_repo, event_repo, analysis_repo, graph_repo
from app.services.pipeline import IntelligencePipeline
from app.api.news_api import router as news_router
from app.api.event_api import router as event_router
from app.api.analysis_api import router as analysis_router
from app.api.graph_api import router as graph_router
from app.api.statistics_api import router as statistics_router

app = FastAPI(title=APP_NAME, version=APP_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(news_router)
app.include_router(event_router)
app.include_router(analysis_router)
app.include_router(graph_router)
app.include_router(statistics_router)


@app.on_event("startup")
def startup_event():
    db_manager.init_db()
    # 首次启动时自动跑一次演示流水线
    if news_repo.count() == 0:
        pipeline = IntelligencePipeline(news_repo, event_repo, analysis_repo, graph_repo)
        pipeline.run_once()


@app.get("/")
def root():
    return {
        "name": APP_NAME,
        "version": APP_VERSION,
        "message": "FinIntel backend is running. Visit /docs for Swagger API."
    }


@app.post("/api/pipeline/run")
def run_pipeline(clear_before_run: bool = False):
    db_manager.init_db()
    if clear_before_run:
        db_manager.clear_all()
    pipeline = IntelligencePipeline(news_repo, event_repo, analysis_repo, graph_repo)
    return pipeline.run_once()
