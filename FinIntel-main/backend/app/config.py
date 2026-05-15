from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "fintel.db"
MOCK_NEWS_PATH = DATA_DIR / "mock_news.json"

APP_NAME = "FinIntel：面向 A 股市场的多源金融情报收集与智能分析系统"
APP_VERSION = "0.1.0"
