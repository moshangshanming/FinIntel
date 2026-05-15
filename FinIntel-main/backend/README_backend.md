# FinIntel 后端说明

## 启动方式

```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

浏览器打开：

- 后端首页：http://127.0.0.1:8000
- Swagger 接口文档：http://127.0.0.1:8000/docs

## 主要接口

- `POST /api/pipeline/run`：运行一次情报处理流水线
- `GET /api/news`：获取新闻列表
- `GET /api/events`：获取事件列表
- `GET /api/analysis`：获取分析结果
- `GET /api/statistics`：获取统计数据
- `GET /api/graph`：获取知识图谱节点和边
