from app.models.news_item import NewsItem
from app.services.news_cleaner import NewsCleaner


def main():
    cleaner = NewsCleaner()

    raw_news = NewsItem(
        title="  【突发】紫金矿业!!! 股价大涨 @@@ <b>利好</b> https://test.com  ",
        content="""
            <p>紫金矿业今日发布公告，&nbsp; 公司业绩增长明显!!!</p>
            更多详情见：https://example.com/news
            市场情绪较强，投资者关注度提升。
        """,
        source="  新浪财经  ",
        publish_time="  2026-05-15 10:30:00  ",
        url="  https://finance.sina.com.cn/test  ",
        stock_code="sh601899",
        stock_name="  紫金矿业  ",
        industry="  有色金属  "
    )

    cleaned_news = cleaner.clean(raw_news)

    print("清洗前：")
    print(raw_news)

    print("\n清洗后：")
    print(cleaned_news)

    print("\n单独字段查看：")
    print("标题：", cleaned_news.title)
    print("正文：", cleaned_news.content)
    print("来源：", cleaned_news.source)
    print("股票代码：", cleaned_news.stock_code)
    print("股票名称：", cleaned_news.stock_name)
    print("行业：", cleaned_news.industry)


if __name__ == "__main__":
    main()