import os
import aiohttp
from dotenv import load_dotenv
from bot.dispatcher import bot

load_dotenv()

WEBHOOK_BASE = os.getenv("WEBHOOK_BASE")  # .env dan o‘qiydi
BOT_TOKEN = os.getenv("BOT_TOKEN")        # Asosiy bot token

# 🔹 Telegram Webhook URL
WEBHOOK_URL = f"{WEBHOOK_BASE}/webhook/testbot"  # FastAPI'dagi webhook endpoint bilan bir xil bo‘lishi kerak


async def set_webhook():
    """
    Telegram bot uchun webhook o‘rnatadi.
    """
    try:
        await bot.set_webhook(WEBHOOK_URL)
        return {"status": "success", "url": WEBHOOK_URL}
    except Exception as e:
        return {"status": "error", "message": str(e)}


async def delete_webhook():
    """
    Webhookni o‘chiradi (polling uchun yoki qayta sozlashdan oldin).
    """
    try:
        await bot.delete_webhook()
        return {"status": "deleted"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


async def register_new_bot(token: str, user_id: int):
    """
    Yangi bot tokenini ro‘yxatdan o‘tkazish uchun FastAPI endpointdan chaqiriladi.
    """
    url = "https://api.telegram.org/bot{}/getMe".format(token)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()

            if not data.get("ok"):
                return {"status": "error", "message": "Token xato yoki bot topilmadi"}

            bot_info = data["result"]
            username = bot_info["username"]
            first_name = bot_info.get("first_name", "Unknown")

            # Bu yerda sen DB ga yozishing mumkin:
            # await save_to_db(user_id, token, username)

            print(f"✅ Bot ro‘yxatdan o‘tdi: @{username} ({first_name})")
            return {"status": "success", "username": username}
