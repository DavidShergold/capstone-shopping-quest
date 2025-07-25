#!/usr/bin/env python3
"""
Environment check script for Shopping Quest
Run this before starting the development server to ensure all dependencies are available.
"""

import sys
import importlib

# Required packages for the application
REQUIRED_PACKAGES = [
    'django',
    'dj_database_url',
    'whitenoise',
    'psycopg2',  # Note: actual package is psycopg2-binary
]

def check_package(package_name):
    """Check if a package is installed and importable."""
    try:
        importlib.import_module(package_name)
        return True, "[OK] Available"
    except ImportError as e:
        return False, f"[ERROR] Missing: {e}"

def main():
    print("Shopping Quest Environment Check")
    print("=" * 50)
    
    all_good = True
    
    for package in REQUIRED_PACKAGES:
        available, status = check_package(package)
        print(f"{package:20} {status}")
        if not available:
            all_good = False
    
    print("=" * 50)
    
    if all_good:
        print("All dependencies are available!")
        print("Safe to run: python manage.py runserver")
    else:
        print("Some dependencies are missing!")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()
