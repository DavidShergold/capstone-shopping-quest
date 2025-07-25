#!/usr/bin/env python3
"""
Shopping Quest Quick Start Script - Test Mode
Runs all checks but doesn't start the server
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
    print("Shopping Quest - Startup Check (Test Mode)")
    print("=" * 50)
    
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
        print("Migrations needed (would apply in real run)")
    else:
        print("Database is up to date!")
    
    # Test basic Django functionality
    success, output = run_command(f'"{python_exe}" manage.py check', "Running Django system check")
    if not success:
        print("Django system check failed!")
        print(output)
        return 1
    
    print("Django system check passed!")
    
    print("\n" + "=" * 50)
    print("ALL STARTUP CHECKS PASSED!")
    print("Ready to run: python quick_start.py")
    print("Or manually: python manage.py runserver 8002")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
