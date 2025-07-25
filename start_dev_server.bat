@echo off
REM Shopping Quest Development Server Startup Script (Windows)
REM This ensures a clean startup every time

echo 🗡️ Shopping Quest - Development Server Startup
echo ================================================

REM Check if virtual environment is activated
if "%VIRTUAL_ENV%"=="" (
    echo ⚠️  Virtual environment not detected!
    echo 💡 Run: venv\Scripts\activate
    pause
    exit /b 1
)

REM Check environment dependencies
echo 🔍 Checking dependencies...
python check_environment.py
if errorlevel 1 (
    echo ❌ Environment check failed!
    pause
    exit /b 1
)

REM Check for migrations
echo 🔄 Checking for pending migrations...
python manage.py migrate --check >nul 2>&1
if errorlevel 1 (
    echo ⚠️  Pending migrations found!
    echo 🔧 Running migrations...
    python manage.py migrate
)

REM Start the development server
echo 🚀 Starting development server...
python manage.py runserver 8002
