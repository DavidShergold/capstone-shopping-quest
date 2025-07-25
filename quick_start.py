#!/usr/bin/env python3
"""
Shopping Quest Quick Start Script
Cross-platform startup script with environment validation
"""

import os
import sys
import subprocess

def run_command(command, description=""):
    """Run a command and return success status."""
    if description:
        print(f"[RUNNING] {description}...")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def main():
    print("Shopping Quest - Quick Start")
    print("=" * 40)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working directory: {script_dir}")
    
    # Use the current Python executable (should be from venv)
    python_exe = sys.executable
    print(f"Using Python: {python_exe}")
    
    # Check environment
    success, output = run_command(f'"{python_exe}" check_environment.py', "Checking dependencies")
    if not success:
        print("Environment check failed!")
        print(output)
        return 1
    
    print("Environment check passed!")
    
    # Check migrations
    success, output = run_command(f'"{python_exe}" manage.py migrate --check', "Checking migrations")
    if not success:
        print("Migrations needed, applying...")
        success, output = run_command(f'"{python_exe}" manage.py migrate', "Applying migrations")
        if not success:
            print("Migration failed!")
            print(output)
            return 1
    
    print("Database is up to date!")
    
    # Start server
    print("\nStarting development server...")
    print("Access at: http://127.0.0.1:8002/")
    print("Press Ctrl+C to stop\n")
    
    try:
        subprocess.run(f'"{python_exe}" manage.py runserver 8002', shell=True, check=True)
    except KeyboardInterrupt:
        print("\nShopping Quest server stopped!")
    except subprocess.CalledProcessError as e:
        print(f"Server failed to start: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
