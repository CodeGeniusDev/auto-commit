# Auto Commit Script 🤖

Automated daily GitHub commit script that keeps your contribution graph active.

## How It Works

This script automatically:
- Updates `python.py` with current date and time
- Creates a commit with a daily message
- Pushes to GitHub

## Quick Start

### Test Manually
```bash
python3 auto_commit.py
```

### Automate with Cron (Mac)

1. Open Terminal:
```bash
crontab -e
```

2. Add this line for daily commits at 10 AM:
```bash
0 10 * * * /usr/bin/python3 /Users/abdullahabad/AbdullahAbbad-Portfolio/Auto-Github/auto_commit.py
```

3. Save and exit (ESC, then :wq)

### Alternative Schedule Options

**Random time between 9 AM - 6 PM:**
```bash
0 9 * * * sleep $((RANDOM \% 32400)) && /usr/bin/python3 /Users/abdullahabad/AbdullahAbbad-Portfolio/Auto-Github/auto_commit.py
```

**Multiple times per day (9 AM, 2 PM, 6 PM):**
```bash
0 9,14,18 * * * /usr/bin/python3 /Users/abdullahabad/AbdullahAbbad-Portfolio/Auto-Github/auto_commit.py
```

## Setup Requirements

- Git configured with your credentials
- For private repos: GitHub Personal Access Token or SSH key
- Python 3.x installed

## Files

- `auto_commit.py` - Main automation script
- `python.py` - File that gets updated daily
- `README.md` - This file

## Troubleshooting

**Permission denied:**
```bash
chmod +x auto_commit.py
```

**Cron not working on Mac:**
Give Terminal Full Disk Access in System Preferences → Security & Privacy → Privacy

---
Made with ❤️ for maintaining GitHub streaks
