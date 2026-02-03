#!/usr/bin/env python3
"""
Automated Daily GitHub Commit Script
Makes multiple random commits throughout the day
"""

import os
import subprocess
from datetime import datetime
import random
import time

# Configuration
REPO_PATH = "/Users/abdullahabad/AbdullahAbbad-Portfolio/Auto-Github"
COMMIT_FILE = "python.py"
BRANCH_NAME = "main"

# Fun quotes/facts for variety
DAILY_CONTENT = [
    "🚀 Coded something cool today",
    "💡 Learned something new", 
    "🎯 Made progress on my project",
    "✨ Improved my codebase",
    "🔧 Fixed some bugs",
    "📚 Studied new concepts",
    "🎨 Worked on design",
    "⚡ Optimized performance",
    "🌟 Added new feature",
    "🔍 Refactored code",
    "📝 Updated documentation",
    "🎉 Completed milestone",
    "🛠️ Enhanced functionality",
    "💻 Improved UI/UX",
    "🔐 Added security improvements"
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


def make_commit():
    """Create and push a single commit"""
    
    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Path to the commit file
    file_path = os.path.join(REPO_PATH, COMMIT_FILE)
    
    # Create simple Python code update with random content
    random_message = random.choice(DAILY_CONTENT)
    random_number = random.randint(1000, 9999)
    
    content = f'''# Auto-generated commit
# Date: {date_str}
# Time: {time_str}
# Commit ID: {random_number}

import random
from datetime import datetime

def daily_update():
    """Daily automated function - {date_str} {time_str}"""
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
    
    print(f"Update #{random_number}: {random_message}")
    print(f"Generated on: {date_str} at {time_str}")
    
    # Additional random functionality
    tasks_completed = random.randint(1, 10)
    print(f"Tasks completed today: {{tasks_completed}}")

if __name__ == "__main__":
    daily_update()
'''
    
    # Write to file
    with open(file_path, 'w') as f:
        f.write(content)
    
    # Git commands
    run_git_command(f"git add {COMMIT_FILE}")
    
    commit_message = f"{random_message} - {date_str}"
    run_git_command(f'git commit -m "{commit_message}"')
    
    run_git_command(f"git push origin {BRANCH_NAME}")
    
    print(f"✅ Commit #{random_number} pushed at {time_str}")
    return True


def make_multiple_commits():
    """Make 4-7 random commits with delays"""
    
    # Random number of commits (4-7)
    num_commits = random.randint(4, 7)
    
    print("🤖 Multi-Commit Script Started")
    print("=" * 50)
    print(f"📊 Planning {num_commits} commits for today")
    print("=" * 50)
    
    for i in range(num_commits):
        try:
            print(f"\n📝 Making commit {i+1}/{num_commits}...")
            make_commit()
            
            # Add delay between commits (except for the last one)
            if i < num_commits - 1:
                # Random delay between 2-10 seconds
                delay = random.randint(2, 10)
                print(f"⏳ Waiting {delay} seconds before next commit...")
                time.sleep(delay)
                
        except Exception as e:
            print(f"❌ Error on commit {i+1}: {e}")
            continue
    
    print("\n" + "=" * 50)
    print(f"✨ Successfully completed {num_commits} commits!")
    print("=" * 50)


def setup_repo():
    """Initialize the repository if needed"""
    if not os.path.exists(REPO_PATH):
        print(f"❌ Repository path not found: {REPO_PATH}")
        return False
    
    print(f"✅ Repository found: {REPO_PATH}")
    return True


if __name__ == "__main__":
    if setup_repo():
        make_multiple_commits()
    else:
        print("\n⚠️  Please configure the script first!")
