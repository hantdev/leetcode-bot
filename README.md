# LeetCode Reminder Bot

## Description

This is a simple bot that will remind you to do a LeetCode problem every day. It will send you a message on Telegram with a link to a random problem from LeetCode.

## Usage

1. Clone the repository

```bash
git clone https://github.com/hantdev/leetcode-bot.git
cd leetcode-bot
```

2. Install the requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file and fill in the required fields

```bash
cp .env.example .env
```

4. Run the bot

```bash
python leetcode-bot.py
```
