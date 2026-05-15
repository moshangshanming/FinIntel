# FinIntel：面向 A 股市场的多源金融情报收集与智能分析系统

## 一、项目简介

FinIntel 是一个面向课程实践提交版本的金融情报分析系统。系统通过模拟财经新闻数据，实现新闻采集、文本清洗、去重融合、智能分析、SQLite 入库、知识图谱构建和前端可视化展示。

本版本采用轻量化部署方案：

- 后端：Python + FastAPI
- 数据库：SQLite
- 前端：Vue3 + ECharts
- 新闻源：本地 `mock_news.json`
- 知识图谱：SQLite 节点表 + 边表模拟 Neo4j

## 二、目录结构

```text
FinIntel/
├── backend/       后端代码
├── frontend/      前端代码
├── docs/          报告和设计文档
├── scripts/       启动脚本
└── README.md      项目总说明
```
项目详细结构
```
FinIntel/
├── backend/                         # 后端项目
│   ├── app/                         # 后端主程序包
│   │   ├── main.py                  # FastAPI 启动入口
│   │   ├── config.py                # 系统配置
│   │   ├── dependencies.py          # 依赖项管理，可选
│   │   │
│   │   ├── models/                  # 数据模型类
│   │   │   ├── __init__.py
│   │   │   ├── news_item.py          # NewsItem 新闻对象
│   │   │   ├── event_item.py         # EventItem 事件对象
│   │   │   ├── analysis_result.py    # AnalysisResult 分析结果对象
│   │   │   ├── stock_relation.py     # StockRelation 股票关联对象
│   │   │   └── graph_model.py        # GraphNode / GraphEdge 图谱对象
│   │   │
│   │   ├── crawlers/                # 新闻采集模块
│   │   │   ├── __init__.py
│   │   │   ├── base_crawler.py       # BaseCrawler 抽象爬虫类
│   │   │   ├── mock_crawler.py       # MockNewsCrawler 模拟新闻采集
│   │   │   ├── sina_crawler.py       # 新浪财经爬虫预留
│   │   │   ├── eastmoney_crawler.py  # 东方财富爬虫预留
│   │   │   ├── ths_crawler.py        # 同花顺爬虫预留
│   │   │   ├── cls_crawler.py        # 财联社爬虫预留
│   │   │   └── crawler_manager.py    # CrawlerManager 多源采集调度器
│   │   │
│   │   ├── services/                # 核心业务逻辑
│   │   │   ├── __init__.py
│   │   │   ├── news_cleaner.py        # NewsCleaner 新闻清洗
│   │   │   ├── deduplicator.py        # DeduplicationService 新闻去重
│   │   │   ├── llm_analyzer.py        # LLMAnalyzer 智能分析
│   │   │   ├── impact_scorer.py       # ImpactScorer 影响评分
│   │   │   ├── risk_scorer.py         # RiskScorer 风险评分
│   │   │   ├── graph_builder.py       # KnowledgeGraphService 图谱构建
│   │   │   └── pipeline.py            # IntelligencePipeline 总流程调度
│   │   │
│   │   ├── repositories/            # 数据库访问层
│   │   │   ├── __init__.py
│   │   │   ├── database.py            # DatabaseManager 数据库连接和建表
│   │   │   ├── news_repository.py     # NewsRepository 新闻表操作
│   │   │   ├── event_repository.py    # EventRepository 事件表操作
│   │   │   ├── analysis_repository.py # AnalysisRepository 分析结果表操作
│   │   │   └── graph_repository.py    # GraphRepository 图谱节点和边操作
│   │   │
│   │   ├── api/                     # 后端接口层
│   │   │   ├── __init__.py
│   │   │   ├── news_api.py            # 新闻相关接口
│   │   │   ├── event_api.py           # 事件相关接口
│   │   │   ├── analysis_api.py        # 分析结果接口
│   │   │   ├── graph_api.py           # 知识图谱接口
│   │   │   └── statistics_api.py      # 统计图表接口
│   │   │
│   │   └── utils/                   # 工具类
│   │       ├── __init__.py
│   │       ├── text_utils.py          # 文本处理工具
│   │       ├── time_utils.py          # 时间处理工具
│   │       ├── hash_utils.py          # 哈希和去重工具
│   │       └── response_utils.py      # API 返回格式工具
│   │
│   ├── data/                        # 后端数据文件
│   │   ├── mock_news.json            # 模拟新闻数据
│   │   ├── stock_list.json           # 股票基础信息，可选
│   │   └── fintel.db                 # SQLite 数据库文件，运行后生成
│   │
│   ├── tests/                       # 后端测试代码
│   │   ├── test_crawler.py
│   │   ├── test_cleaner.py
│   │   ├── test_analyzer.py
│   │   └── test_database.py
│   │
│   ├── requirements.txt             # Python 依赖
│   ├── init_db.py                   # 初始化数据库脚本
│   ├── run_backend.bat              # Windows 后端启动脚本
│   └── README_backend.md            # 后端说明文档
│
├── frontend/                        # 前端项目
│   ├── src/
│   │   ├── main.js                  # 前端入口
│   │   ├── App.vue                  # 根组件
│   │   │
│   │   ├── api/                     # 前端请求接口
│   │   │   ├── request.js            # Axios 封装
│   │   │   ├── news.js               # 新闻接口请求
│   │   │   ├── analysis.js           # 分析接口请求
│   │   │   ├── graph.js              # 图谱接口请求
│   │   │   └── statistics.js         # 统计接口请求
│   │   │
│   │   ├── views/                   # 页面
│   │   │   ├── Dashboard.vue         # 首页仪表盘
│   │   │   ├── NewsList.vue          # 新闻情报列表页
│   │   │   ├── StockDetail.vue       # 股票详情分析页
│   │   │   ├── KnowledgeGraph.vue    # 知识图谱展示页
│   │   │   └── SystemMonitor.vue     # 系统运行监控页
│   │   │
│   │   ├── components/              # 页面组件
│   │   │   ├── NewsCard.vue          # 新闻卡片
│   │   │   ├── ScoreTag.vue          # 评分标签
│   │   │   ├── SourceChart.vue       # 新闻来源柱状图
│   │   │   ├── SentimentChart.vue    # 情绪分布图
│   │   │   ├── ImpactRankChart.vue   # 影响分排行榜
│   │   │   ├── RiskChart.vue         # 风险分布图
│   │   │   └── GraphView.vue         # 图谱组件
│   │   │
│   │   ├── router/                  # 路由
│   │   │   └── index.js
│   │   │
│   │   └── assets/                  # 静态资源
│   │       └── logo.png
│   │
│   ├── public/
│   ├── package.json
│   ├── vite.config.js
│   ├── run_frontend.bat
│   └── README_frontend.md
│
├── docs/                            # 报告和文档
│   ├── 实践报告.docx
│   ├── 项目概述.md
│   ├── 需求分析.md
│   ├── 系统设计.md
│   ├── 数据库设计.md
│   ├── 接口说明文档.md
│   ├── 类图设计.md
│   ├── 每日进度记录.md
│   ├── 任务分工表.md
│   │
│   ├── diagrams/                    # 图
│   │   ├── 系统架构图.png
│   │   ├── 系统流程图.png
│   │   ├── 功能结构图.png
│   │   ├── 类图.png
│   │   └── 数据库ER图.png
│   │
│   └── screenshots/                 # 运行截图
│       ├── 01_后端启动截图.png
│       ├── 02_Swagger接口截图.png
│       ├── 03_数据库截图.png
│       ├── 04_首页仪表盘截图.png
│       ├── 05_新闻列表截图.png
│       ├── 06_股票详情截图.png
│       └── 07_知识图谱截图.png
│
├── scripts/                         # 辅助脚本
│   ├── run_all.bat                  # 一键启动脚本
│   ├── clean_cache.bat              # 清理缓存脚本
│   └── export_demo_data.py          # 导出演示数据，可选
│
├── README.md                        # 总说明文档
└── 项目提交说明.txt
```
## 三、后端启动

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

打开：

```text
http://127.0.0.1:8000/docs
```

## 四、前端启动

```bash
cd frontend
npm install
npm run dev
```

打开：

```text
http://127.0.0.1:5173
```

## 五、主要功能

1. 多源财经新闻采集接口设计；
2. 模拟新闻数据读取；
3. 新闻清洗与标准化；
4. 新闻标题相似度去重；
5. 基于规则模拟 LLM 情绪分析、影响评分和风险评分；
6. SQLite 数据库存储；
7. 轻量级知识图谱构建；
8. 前端仪表盘、新闻列表、分析结果和知识图谱展示。

## 六、小组分工

- zsm：系统架构、核心类设计、报告整合、答辩；
- yjq：新闻采集模块；
- rsr：数据库和后端 API；
- hrq：前端和可视化图表。

## 七、课程提交说明

本项目提交版本避免强依赖 Neo4j、MySQL、Redis 等外部服务，使用 SQLite 和本地模拟数据保证稳定运行。后续增强版本可进一步接入真实财经爬虫、Neo4j 图数据库和真实大语言模型 API。
