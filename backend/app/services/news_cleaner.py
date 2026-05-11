from app.models.news_item import NewsItem
from app.utils.text_utils import clean_text


class NewsCleaner:
    """新闻清洗器：统一清洗标题、正文、来源等字段。"""

    def clean(self, news: NewsItem) -> NewsItem:
        return NewsItem(
            title=clean_text(news.title),
            content=clean_text(news.content),
            source=clean_text(news.source),
            publish_time=clean_text(news.publish_time),
            url=clean_text(news.url),
            stock_code=clean_text(news.stock_code),
            stock_name=clean_text(news.stock_name),
            industry=clean_text(news.industry),
        )
