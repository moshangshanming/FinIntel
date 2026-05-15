from app.main_dependencies import db_manager, news_repo, event_repo, analysis_repo, graph_repo
from app.services.pipeline import IntelligencePipeline


def test_pipeline_run():
    db_manager.init_db()
    db_manager.clear_all()
    pipeline = IntelligencePipeline(news_repo, event_repo, analysis_repo, graph_repo)
    result = pipeline.run_once()
    assert result["raw_news_count"] > 0
    assert result["unique_event_count"] > 0
