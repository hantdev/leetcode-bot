import os
import json
import random
import asyncio
import schedule
import requests
from datetime import datetime, timedelta
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN") 
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
STREAK_FILE = "streak.json"

bot = Bot(token=TOKEN)

def get_random_problem():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        problems = data.get("stat_status_pairs", [])
        if problems:
            problem = random.choice(problems) 
            title = problem["stat"]["question__title"]
            slug = problem["stat"]["question__title_slug"]
            difficulty = problem["difficulty"]["level"]
            difficulty_map = {1: "🟢 Easy", 2: "🟡 Medium", 3: "🔴 Hard"}
            problem_link = f"https://leetcode.com/problems/{slug}/"
            return title, problem_link, difficulty_map.get(difficulty, 'Unknown')
    return None, None, None

def load_streak():
    if os.path.exists(STREAK_FILE):
        with open(STREAK_FILE, "r") as f:
            return json.load(f)
    return {"streak": 0, "last_date": None}

def save_streak(streak_data):
    with open(STREAK_FILE, "w") as f:
        json.dump(streak_data, f)

def update_streak():
    streak_data = load_streak()
    today = datetime.now().strftime("%Y-%m-%d")
    last_date = streak_data.get("last_date")

    if last_date:
        last_date_obj = datetime.strptime(last_date, "%Y-%m-%d")
        if last_date_obj == datetime.now() - timedelta(days=1):
            streak_data["streak"] += 1 
        elif last_date_obj < datetime.now() - timedelta(days=1):
            streak_data["streak"] = 1 
    else:
        streak_data["streak"] = 1

    streak_data["last_date"] = today
    save_streak(streak_data)
    return streak_data["streak"]

async def send_reminder():
    title, problem_link, difficulty = get_random_problem()
    if not title:
        message = "Không thể lấy bài LeetCode hôm nay. Hãy thử lại sau! 😢"
    else:
        streak = update_streak()
        message = (
            "🔔 **Đã đến giờ làm LeetCode!**\n\n"
            f"🚀 Hôm nay hãy thử giải bài: [{title}]({problem_link})\n"
            f"🔹 Độ khó: {difficulty}\n\n"
            f"🔥 Streak hiện tại: **{streak} ngày liên tiếp!**\n"
            "📈 Đừng để streak bị reset nhé! 💪"
        )

    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

def schedule_reminders():
    schedule.every().day.at("08:00").do(lambda: asyncio.run(send_reminder()))
    # schedule.every().day.at("12:00").do(lambda: asyncio.run(send_reminder()))
    # schedule.every().day.at("18:00").do(lambda: asyncio.run(send_reminder()))

async def main():
    print("📢 Bot nhắc nhở LeetCode đang chạy!")
    # await send_reminder()  # Gửi thông báo ngay khi chạy
    schedule_reminders()

    while True:
        schedule.run_pending()
        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
