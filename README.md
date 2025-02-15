# LeetCode Reminder Bot

## Description

This is a simple bot that will remind you to do a LeetCode problem every day. It will send you a message on Telegram with a link to a random problem from LeetCode.

## Usage

1. Create a new bot on Telegram using the [BotFather](https://core.telegram.org/bots#6-botfather)

**Bot Token** - The token that the BotFather gives you when you create the bot

![alt text](<./img/1.png>)

2. Get your chat ID using Bot `@userinfobot`

**Chat ID** - The ID that the @userinfobot gives you when you start a chat with it

![alt text](<./img/2.png>)

3. Clone the repository

```bash
git clone https://github.com/hantdev/leetcode-bot.git
cd leetcode-bot
```

4. Install the requirements

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Create a `.env` file and fill in the required fields

```bash
cp .env.example .env
```

6. Run the bot with `tmux`

Install tmux if you don't have it

```bash
sudo apt install tmux # Ubuntu/Debian
sudo yum install tmux # CentOS/RHEL
```

```bash
tmux new -s leetcode-bot
source venv/bin/activate
python leetcode-bot.py
```

7. To detach from the tmux session, press `Ctrl + B` and then `D`
8. To attach to the tmux session, run `tmux attach -t leetcode-bot`
