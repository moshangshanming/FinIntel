from app.models.news_item import NewsItem
from app.services.news_cleaner import NewsCleaner


def test_cleaner():
    item = NewsItem("<b>测试标题</b>", "  测试   内容 ", "来源", "2026-05-11", "url")
    cleaned = NewsCleaner().clean(item)
    assert cleaned.title == "测试标题"
    assert cleaned.content == "测试 内容"
