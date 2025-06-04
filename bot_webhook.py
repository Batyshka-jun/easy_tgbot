from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

BOT_TOKEN = "7093125966:AAFsOb8PPAJf70XgdN6glLdrve_K7UKPujs"
WEBHOOK_URL = "https://yourdomain.onrender.com/bot"   # Замени на свой URL

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет от бота с вебхуком!")

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)

dp.startup.register(on_startup)

app = web.Application()
SimpleRequestHandler(dispatcher=dp, bot=bot).register(app)
setup_application(app, dp, bot=bot)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)