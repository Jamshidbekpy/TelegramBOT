from fastapi import FastAPI, Request
from aiogram.types import Update
from contextlib import asynccontextmanager
from bot_manager import set_webhook
from bot.dispatcher import dp, bot
from bot.handlers import router
from bot.middlewares import LoggingMiddleware


# 🧠 Lifespan — bu yangi startup/shutdown tizimi
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Bot ishga tushmoqda...")
    result = await set_webhook()
    print("🔗 Webhook o‘rnatildi:", result)
    yield
    print("🛑 Server to‘xtatildi.")


# FastAPI app yaratish
app = FastAPI(lifespan=lifespan)


# 🔹 Router va Middleware ulaymiz
dp.include_router(router)
dp.message.middleware(LoggingMiddleware())


# 🔹 Telegram yuboradigan webhook endpoint
@app.post("/webhook/testbot")
async def telegram_webhook(data: dict):
    # 1. Lug'atni (dict) Update obyektiga o'tkazamiz
    update = Update.model_validate(data, context={"bot": bot})

    # 2. Obyektni dispatcher'ga yuboramiz (webhook uchun to'g'ri metod)
    await dp.feed_webhook_update(bot=bot, update=update)
    
    return {"ok": True}
