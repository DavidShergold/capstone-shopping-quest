#!/bin/bash
# Shopping Quest Development Server Startup Script
# This ensures a clean startup every time

echo "🗡️ Shopping Quest - Development Server Startup"
echo "================================================"

# Check if virtual environment is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "⚠️  Virtual environment not detected!"
    echo "💡 Run: source venv/Scripts/activate (Windows) or source venv/bin/activate (Mac/Linux)"
    exit 1
fi

# Check environment dependencies
echo "🔍 Checking dependencies..."
python check_environment.py
if [ $? -ne 0 ]; then
    echo "❌ Environment check failed!"
    exit 1
fi

# Check for migrations
echo "🔄 Checking for pending migrations..."
python manage.py showmigrations --plan | grep -q '\[ \]'
if [ $? -eq 0 ]; then
    echo "⚠️  Pending migrations found!"
    echo "🔧 Running migrations..."
    python manage.py migrate
fi

# Start the development server
echo "🚀 Starting development server..."
python manage.py runserver 8002
