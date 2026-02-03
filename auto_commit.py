#!/usr/bin/env python3
"""
Automated Daily GitHub Commit Script
Makes a commit to your repository with daily updates
"""

import os
import subprocess
from datetime import datetime
import random

# Configuration
REPO_PATH = "/Users/abdullahabad/AbdullahAbbad-Portfolio/Auto-Github"
COMMIT_FILE = "python.py"          # File that will be updated daily
BRANCH_NAME = "main"               # Change to 'master' if needed

# Fun quotes/facts for variety (optional)
DAILY_CONTENT = [
    "Coded something cool today",
    "Learned something new",
    "Made progress on my project",
    "Improved my codebase",
    "Fixed some bugs",
    "Studied new concepts",
    "Worked on design",
    "Optimized performance",
]


def run_git_command(command, cwd=REPO_PATH):
    """Execute a git command and return the output"""
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return None


def make_daily_commit():
    """Create and push a daily commit"""
    
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Path to the commit file
    file_path = os.path.join(REPO_PATH, COMMIT_FILE)
    
    # Create simple Python code update
    content = f'''# Auto-generated daily commit
# Date: {date_str}
# Time: {time_str}

import random
from datetime import datetime

def daily_update():
    """Daily automated function - {date_str}"""
    messages = [
        "🚀 Coded something cool today",
        "💡 Learned something new", 
        "🎯 Made progress on my project",
        "✨ Improved my codebase",
        "🔧 Fixed some bugs",
        "📚 Studied new concepts",
        "🎨 Worked on design",
        "⚡ Optimized performance"
    ]
    
    print(f"Update #{random.randint(1000, 9999)}: {{random.choice(messages)}}")
    print(f"Generated on: {date_str} at {time_str}")

if __name__ == "__main__":
    daily_update()
'''
    
    # Write to file (overwrite each time)
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated {COMMIT_FILE}")
    
    # Git commands
    print("📝 Adding changes...")
    run_git_command(f"git add {COMMIT_FILE}")
    
    print("💾 Creating commit...")
    commit_message = f"Daily update: {date_str}"
    run_git_command(f'git commit -m "{commit_message}"')
    
    print("🚀 Pushing to GitHub...")
    run_git_command(f"git push origin {BRANCH_NAME}")
    
    print(f"✨ Successfully committed and pushed on {date_str}!")


def setup_repo():
    """Initialize the repository if needed"""
    if not os.path.exists(REPO_PATH):
        print(f"❌ Repository path not found: {REPO_PATH}")
        print("Please update REPO_PATH in the script")
        return False
    
    # python.py will be created/overwritten by make_daily_commit
    print(f"✅ Repository found: {REPO_PATH}")
    
    return True


if __name__ == "__main__":
    print("🤖 Auto Commit Script Started")
    print("=" * 50)
    
    if setup_repo():
        make_daily_commit()
    else:
        print("\n⚠️  Please configure the script first!")
        print("1. Update REPO_PATH to your repository location")
        print("2. Make sure git is configured with your credentials")