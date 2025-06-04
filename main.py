# main.py

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

bot = Bot(token="7093125966:AAHBahHedhuO1yQOGEFzdFJKIthxPaIPVMY")
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Бот работает через вебхук.")

app = web.Application()
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app)
setup_application(app, dp, bot=bot)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
