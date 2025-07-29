#!/usr/bin/env python3
"""
PEP8 Fix Script for Shopping Quest
Automatically fixes common PEP8 violations found by flake8
"""

import os
import re

def fix_pep8_issues():
    """Fix common PEP8 issues in the quests app"""
    
    # Files to fix
    files_to_fix = [
        'quests/admin.py',
        'quests/forms.py', 
        'quests/models.py',
        'quests/urls.py',
        'quests/views.py'
    ]
    
    for file_path in files_to_fix:
        if os.path.exists(file_path):
            print(f"Fixing {file_path}...")
            fix_file(file_path)
        else:
            print(f"File not found: {file_path}")

def fix_file(file_path):
    """Fix PEP8 issues in a single file"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix whitespace issues
    content = fix_whitespace_issues(content)
    
    # Fix line length issues
    content = fix_line_length_issues(content)
    
    # Fix import and class spacing
    content = fix_spacing_issues(content)
    
    # Add newline at end of file
    if not content.endswith('\n'):
        content += '\n'
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Fixed {file_path}")

def fix_whitespace_issues(content):
    """Remove trailing whitespace and fix blank lines with whitespace"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Remove trailing whitespace
        line = line.rstrip()
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_line_length_issues(content):
    """Fix lines that are too long"""
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        if len(line) > 88:
            # Try to break long lines at logical points
            if 'list_display' in line and '[' in line:
                # Break list_display lines
                fixed_line = break_list_display(line)
                fixed_lines.append(fixed_line)
            elif 'path(' in line:
                # Break URL patterns
                fixed_line = break_url_pattern(line)
                fixed_lines.append(fixed_line)
            elif 'get_object_or_404' in line:
                # Break long function calls
                fixed_line = break_function_call(line)
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)  # Keep as is for now
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def break_list_display(line):
    """Break long list_display lines"""
    if 'list_display' in line and len(line) > 88:
        indent = len(line) - len(line.lstrip())
        return line  # Return as-is for now, manual fix needed
    return line

def break_url_pattern(line):
    """Break long URL pattern lines"""
    return line  # Return as-is for now, manual fix needed

def break_function_call(line):
    """Break long function call lines"""
    return line  # Return as-is for now, manual fix needed

def fix_spacing_issues(content):
    """Fix spacing between imports, classes, and functions"""
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Add 2 blank lines before class definitions (except first line)
        if line.startswith('class ') and i > 0:
            # Check if we already have enough blank lines
            prev_non_empty = None
            blank_count = 0
            for j in range(i-1, -1, -1):
                if lines[j].strip():
                    prev_non_empty = j
                    break
                blank_count += 1
            
            if prev_non_empty is not None and blank_count < 2:
                # Add missing blank lines
                while blank_count < 2:
                    fixed_lines.append('')
                    blank_count += 1
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

if __name__ == '__main__':
    print("🔧 Fixing PEP8 issues in Shopping Quest...")
    fix_pep8_issues()
    print("✅ PEP8 fixes completed!")
    print("\n💡 Note: Some long lines may need manual adjustment for optimal readability.")
    print("Run 'python -m flake8 quests/ --max-line-length=88 --exclude=migrations' to check results.")
