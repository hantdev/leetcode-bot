# LeetCode Reminder Bot

## Description

This is a simple bot that will remind you to do a LeetCode problem every day. It will send you a message on Telegram with a link to a random problem from LeetCode.

## Usage

### 1. How to get a Telegram bot token

- In Telegram, search for the user `@BotFather`.
- Use the command `\newbot` and choose a name and username for your bot.
- `@BotFather` will return you the token of the bot created. Remember to keep it safe!

![alt text](<./img/1.png>)

### 2. How to get a Telegram chat ID

- Send a `/start` command to the telegram bot created in the previous step
- Visit `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates`
- Look at the API response, `result[0]['message']['chat']['id']` should contains ID of the chat. Remember to copy the `-` prefix if exists.

> Or you can use the `@userinfobot` to get the chat ID.

![alt text](<./img/2.png>)

### 3. Test if Bot token and Chat ID is correct or not

Open Terminal, run the following command. You will need to replace `<BOT_TOKEN>` and `<CHAT_ID>` with the one you get in previous steps.

```bash
curl -X POST "https://api.telegram.org/bot<BOT_TOKEN>/sendMessage" -d "chat_id=<CHAT_ID>&text=Hello World"
```

### 4. Clone the repository

```bash
git clone https://github.com/hantdev/leetcode-bot.git
cd leetcode-bot
```

### 5. Set up the virtual environment and install the dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 6. Create a `.env` file and fill in the required fields

```bash
cp .env.example .env
```

```bash
TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>
TELEGRAM_CHAT_ID=<YOUR_TELEGRAM_CHAT_ID>
```

### 7. Run the bot with `tmux` if you want to keep it running in the background even after closing the terminal session (Optional)

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

### 8. To detach from the tmux session, press `Ctrl + B` and then `D`

### 9. To attach to the tmux session, run `tmux attach -t leetcode-bot`
