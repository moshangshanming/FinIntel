import json
from typing import Dict, Any, List
from app.repositories.database import DatabaseManager


class GraphRepository:
    """知识图谱节点和边操作类。"""

    def __init__(self, db: DatabaseManager):
        self.db = db

    def upsert_node(self, node_id: str, name: str, node_type: str, properties: Dict[str, Any]) -> None:
        with self.db.connect() as conn:
            conn.execute("""
                INSERT INTO kg_nodes (node_id, name, node_type, properties)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(node_id) DO UPDATE SET
                    name = excluded.name,
                    node_type = excluded.node_type,
                    properties = excluded.properties
            """, (node_id, name, node_type, json.dumps(properties, ensure_ascii=False)))
            conn.commit()

    def upsert_edge(self, source_id: str, target_id: str, relation_type: str, weight: float, properties: Dict[str, Any]) -> None:
        with self.db.connect() as conn:
            conn.execute("""
                INSERT OR IGNORE INTO kg_edges (source_id, target_id, relation_type, weight, properties)
                VALUES (?, ?, ?, ?, ?)
            """, (source_id, target_id, relation_type, weight, json.dumps(properties, ensure_ascii=False)))
            conn.commit()

    def get_graph(self) -> Dict[str, List[Dict[str, Any]]]:
        with self.db.connect() as conn:
            nodes = [dict(row) for row in conn.execute("SELECT * FROM kg_nodes").fetchall()]
            edges = [dict(row) for row in conn.execute("SELECT * FROM kg_edges").fetchall()]

        for node in nodes:
            try:
                node["properties"] = json.loads(node.get("properties") or "{}")
            except json.JSONDecodeError:
                node["properties"] = {}

        for edge in edges:
            try:
                edge["properties"] = json.loads(edge.get("properties") or "{}")
            except json.JSONDecodeError:
                edge["properties"] = {}

        return {"nodes": nodes, "edges": edges}
