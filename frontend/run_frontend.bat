@echo off
chcp 65001 >nul
echo 正在启动 FinIntel 前端页面...
cd /d %~dp0
npm install
npm run dev
pause
