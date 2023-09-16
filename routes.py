from fastapi import Request
from main import app, router

from tg_api import set_webhook
from aiogram import types, Dispatcher, Bot
from aiogram.types import WebAppInfo
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["TOKEN"] # получаем занчения переменных
URL = os.environ["URL"]

WEBHOOK_PATH = f"/bot/{TOKEN}" # формируем системные переменные из переменных окружения
WEBHOOK_URL = URL + WEBHOOK_PATH
print(WEBHOOK_URL)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@router.get('/')
def root():
    return 'OK', 200


@app.on_event("startup") #обработчик запуска приложения, засылает вебхук в телеграм
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@dp.message_handler(commands="start")
async def new_message(message: types.Message):
    text = 'test message'
    keyboard = types.InlineKeyboardMarkup()
    await bot.send_message(message.chat.id, text, reply_markup=keyboard)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)
