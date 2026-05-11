from typing import List, Dict, Any
from app.models.analysis_result import AnalysisResult
from app.repositories.database import DatabaseManager


class AnalysisRepository:
    """分析结果表操作类。"""

    def __init__(self, db: DatabaseManager):
        self.db = db

    def insert_analysis(self, analysis: AnalysisResult) -> None:
        with self.db.connect() as conn:
            conn.execute("""
                INSERT INTO analysis_results
                (event_id, sentiment, sentiment_score, impact_score, risk_score, confidence_score,
                 related_stock_code, related_stock_name, related_industry,
                 analysis_reason, summary, event_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                analysis.event_id, analysis.sentiment, analysis.sentiment_score,
                analysis.impact_score, analysis.risk_score, analysis.confidence_score,
                analysis.related_stock_code, analysis.related_stock_name, analysis.related_industry,
                analysis.analysis_reason, analysis.summary, analysis.event_type
            ))
            conn.commit()

    def list_analysis(self, limit: int = 100) -> List[Dict[str, Any]]:
        with self.db.connect() as conn:
            rows = conn.execute("""
                SELECT a.*, e.event_title
                FROM analysis_results a
                LEFT JOIN events e ON a.event_id = e.event_id
                ORDER BY a.created_at DESC, a.analysis_id DESC
                LIMIT ?
            """, (limit,)).fetchall()
            return [dict(row) for row in rows]

    def statistics(self) -> Dict[str, Any]:
        with self.db.connect() as conn:
            sentiment_rows = conn.execute("""
                SELECT sentiment, COUNT(*) AS count
                FROM analysis_results
                GROUP BY sentiment
            """).fetchall()

            source_rows = conn.execute("""
                SELECT source, COUNT(*) AS count
                FROM news_raw
                GROUP BY source
                ORDER BY count DESC
            """).fetchall()

            industry_rows = conn.execute("""
                SELECT related_industry AS industry, ROUND(AVG(impact_score), 2) AS avg_impact, COUNT(*) AS count
                FROM analysis_results
                GROUP BY related_industry
                ORDER BY avg_impact DESC
            """).fetchall()

            top_impact_rows = conn.execute("""
                SELECT e.event_title, a.impact_score, a.risk_score, a.related_stock_name
                FROM analysis_results a
                LEFT JOIN events e ON a.event_id = e.event_id
                ORDER BY a.impact_score DESC
                LIMIT 10
            """).fetchall()

            return {
                "sentiment_distribution": [dict(row) for row in sentiment_rows],
                "source_distribution": [dict(row) for row in source_rows],
                "industry_impact": [dict(row) for row in industry_rows],
                "top_impact_events": [dict(row) for row in top_impact_rows],
            }
