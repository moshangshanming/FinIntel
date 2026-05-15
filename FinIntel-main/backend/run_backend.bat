@echo off
chcp 65001 >nul
echo 正在启动 FinIntel 后端服务...
cd /d %~dp0
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
pause
