@echo off
REM Simple Shopping Quest Startup Script
echo 🗡️ Shopping Quest - Quick Start
echo ================================

REM Check environment
echo 🔍 Checking dependencies...
C:/Users/sherg/Desktop/vs-code-projects/capstone-shopping-quest/venv/Scripts/python.exe check_environment.py
if errorlevel 1 (
    echo ❌ Environment check failed!
    pause
    exit /b 1
)

REM Check migrations
echo 🔄 Checking migrations...
C:/Users/sherg/Desktop/vs-code-projects/capstone-shopping-quest/venv/Scripts/python.exe manage.py migrate --check
if errorlevel 1 (
    echo ⚠️  Running migrations...
    C:/Users/sherg/Desktop/vs-code-projects/capstone-shopping-quest/venv/Scripts/python.exe manage.py migrate
)

echo ✅ All checks passed!
echo 🚀 Starting development server on port 8002...
echo 💡 Access at: http://127.0.0.1:8002/
echo ⏹️  Press Ctrl+C to stop
echo.
C:/Users/sherg/Desktop/vs-code-projects/capstone-shopping-quest/venv/Scripts/python.exe manage.py runserver 8002
