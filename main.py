from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

# 🔐 Вписываем токен прямо в код
BOT_TOKEN = "7093125966:AAHBahHedhuO1yQOGEFzdFJKIthxPaIPVMY"

# Инициализируем бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Пример обработчика команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я работаю через вебхук!")

@dp.message(Command("help")
async def help(message: Message):
    await message.answer("Задайте свой вопрос")
# Создаем веб-приложение
app = web.Application()

# Регистрируем хендлер с указанием пути "/bot"
SimpleRequestHandler(dispatcher=dp, bot=bot, path="/bot").register(app, path="/bot")

# Настраиваем приложение
setup_application(app, dp, bot=bot)

# Точка входа
if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=8080)
