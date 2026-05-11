import re
from typing import List


def clean_text(text: str) -> str:
    """基础文本清洗：去除多余空白和简单 HTML 标签。"""
    if not text:
        return ""
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def simple_tokenize(text: str) -> List[str]:
    """简化关键词切分：保留中文、英文、数字连续片段。"""
    if not text:
        return []
    return re.findall(r"[\u4e00-\u9fa5A-Za-z0-9]+", text)
