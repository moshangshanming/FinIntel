import hashlib


def md5_text(text: str) -> str:
    text = text or ""
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def simhash_like(text: str) -> str:
    """课程提交版简化实现：返回正文哈希，可后续替换为真正 SimHash。"""
    return md5_text("".join((text or "").split()))
