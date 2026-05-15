from difflib import SequenceMatcher
from typing import List, Tuple, Dict, Set
from app.models.news_item import NewsItem


class DeduplicationService:
    """新闻去重服务：根据股票代码、标题相似度和中文双字片段相似度合并重复新闻。"""

    def __init__(self, threshold: float = 0.52, bigram_threshold: float = 0.18):
        self.threshold = threshold
        self.bigram_threshold = bigram_threshold

    def _similarity(self, a: str, b: str) -> float:
        return SequenceMatcher(None, a or "", b or "").ratio()

    def _bigrams(self, text: str) -> Set[str]:
        text = "".join((text or "").split())
        return {text[i:i + 2] for i in range(max(0, len(text) - 1))}

    def _bigram_jaccard(self, a: str, b: str) -> float:
        a_set = self._bigrams(a)
        b_set = self._bigrams(b)
        if not a_set or not b_set:
            return 0.0
        return len(a_set & b_set) / len(a_set | b_set)

    def _is_duplicate(self, item: NewsItem, existed: NewsItem) -> bool:
        # 课程提交版本的去重逻辑：同一股票 + 标题相似，视为同一事件的多源报道。
        same_stock = bool(item.stock_code and item.stock_code == existed.stock_code)
        if not same_stock:
            return False

        seq_sim = self._similarity(item.title, existed.title)
        bigram_sim = self._bigram_jaccard(item.title, existed.title)
        return seq_sim >= self.threshold or bigram_sim >= self.bigram_threshold

    def deduplicate(self, news_items: List[NewsItem]) -> Tuple[List[NewsItem], Dict[str, int]]:
        unique_items: List[NewsItem] = []
        duplicate_map: Dict[str, int] = {}

        for item in news_items:
            matched_index = None
            for idx, existed in enumerate(unique_items):
                if self._is_duplicate(item, existed):
                    matched_index = idx
                    break

            if matched_index is None:
                unique_items.append(item)
                duplicate_map[item.title] = 1
            else:
                duplicate_map[unique_items[matched_index].title] += 1

        return unique_items, duplicate_map
