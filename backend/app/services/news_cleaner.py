from app.models.news_item import NewsItem
import re


class NewsCleaner:
    """新闻清洗器：统一清洗标题、正文、来源等字段。"""

    def clean(self, news: NewsItem) -> NewsItem:
        return NewsItem(
            title=self.clean_title(news.title),
            content=self.clean_content(news.content),
            source=self.clean_basic(news.source),
            publish_time=self.clean_basic(news.publish_time),
            url=self.clean_basic(news.url),
            stock_code=self.clean_stock_code(news.stock_code),
            stock_name=self.clean_basic(news.stock_name),
            industry=self.clean_basic(news.industry),
        )

    def clean_basic(self, text: str) -> str:
        """基础清洗：去前后空白、换行"""
        if not text:
            return ""
        return text.strip()

    def clean_title(self, text: str) -> str:
        """标题严格清洗：去特殊符号、去多余空格、精简"""
        if not text:
            return "无标题"
        # 去前后空格
        text = text.strip()
        # 把多个空格变成一个
        text = re.sub(r'\s+', ' ', text)
        # 去除常见特殊符号（@#$&*等）
        text = re.sub(r'[!@#$%^&*()_+|{}[\]:;<>,.?~`]', '', text)
        # 去除HTML标签
        text = re.sub(r'<.*?>', '', text)
        # 去除URL链接
        text = re.sub(r'https?://\S+', '', text)
        # 限制标题长度，避免过长
        if len(text) > 100:
            text = text[:100] + "..."
        return text.strip()

    def clean_content(self, text: str) -> str:
        """正文清洗：去HTML标签、去多余空行、去特殊符号"""
        if not text:
            return ""
        # 去除HTML标签
        text = re.sub(r'<.*?>', '', text)
        # 去除HTML实体（&nbsp; &amp;等）
        text = re.sub(r'&[a-z0-9]+;', '', text)
        # 去除URL链接
        text = re.sub(r'https?://\S+', '', text)
        # 去除特殊符号（@#$&*等）
        text = re.sub(r'[!@#$%^&*()_+|{}[\]:;<>,.?~`]', '', text)
        # 把多个换行、空格变成一个空格
        text = re.sub(r'\s+', ' ', text)
        return text.strip()

    def clean_stock_code(self, code: str) -> str:
        """股票代码只保留数字"""
        if not code:
            return ""
        # 只保留数字部分
        return re.sub(r'\D', '', code)