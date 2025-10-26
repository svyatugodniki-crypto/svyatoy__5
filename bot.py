import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import F
from dotenv import load_dotenv
import asyncio

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("🔥 Добро пожаловать в Rap Battle Arena!\n\nЗдесь скоро начнётся настоящий турнир рэперастов. Пока можешь просто кидать /help.")

@dp.message(F.text.lower() == "/help")
async def help_command(message: Message):
    await message.answer("📜 Команды:\n/start — начать\n/help — помощь\n\n(тут потом появится регистрация, отправка треков и всё мясо)")

@dp.message(F.text)
async def echo(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer(f"👑 Админ сказал: {message.text}")
    else:
        await message.answer("Ты пока не в батле, брат. Потерпи.")

async def main():
    print("Бот запущен…")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
