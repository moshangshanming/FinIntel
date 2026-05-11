@echo off
chcp 65001 >nul
echo 将分别启动后端和前端窗口...
start cmd /k "cd /d %~dp0..\backend && python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000"
start cmd /k "cd /d %~dp0..\frontend && npm install && npm run dev"
pause
