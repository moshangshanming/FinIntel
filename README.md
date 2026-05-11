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

## 六、小组建议分工

- zsm：系统架构、核心类设计、报告整合、答辩；
- rsr：新闻采集模块；
- yjq：数据库和后端 API；
- hrq：前端和可视化图表。

## 七、课程提交说明

本项目提交版本避免强依赖 Neo4j、MySQL、Redis 等外部服务，使用 SQLite 和本地模拟数据保证稳定运行。后续增强版本可进一步接入真实财经爬虫、Neo4j 图数据库和真实大语言模型 API。
