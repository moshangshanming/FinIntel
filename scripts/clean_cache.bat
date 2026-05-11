@echo off
chcp 65001 >nul
echo 正在清理 Python 缓存...
for /d /r .. %%d in (__pycache__) do @if exist "%%d" rd /s /q "%%d"
echo 清理完成。
pause
