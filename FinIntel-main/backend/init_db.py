from app.main_dependencies import db_manager

if __name__ == "__main__":
    db_manager.init_db()
    print("SQLite 数据库初始化完成：backend/data/fintel.db")
