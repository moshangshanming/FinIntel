from dataclasses import dataclass, asdict
from typing import Dict, Any


@dataclass
class GraphNode:
    """知识图谱节点。"""
    node_id: str
    name: str
    node_type: str
    properties: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class GraphEdge:
    """知识图谱关系边。"""
    source_id: str
    target_id: str
    relation_type: str
    weight: float
    properties: Dict[str, Any]

    def to_dict(self) -> dict:
        return asdict(self)
