import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode

# ===== ТВОЙ ТОКЕН =====
BOT_TOKEN = "8861133969:AAF8UkV6VbDCOiL5kyEmVA2pkYEIqc-bFk4"
# ======================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    text = (
        "🚀 *Привет! Начинай зарабатывать с Toxic Game!* 💰\n\n"
        "🔥 Подпишись на наши каналы, чтобы быть в курсе:\n"
        "📢 Канал — новости и обновления\n"
        "💬 Чат — общение и помощь\n\n"
        "👇 А затем жми на кнопку *Играть* и начинай зарабатывать прямо сейчас!"
    )
    
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="📢 Подписаться на канал", 
                    url="https://t.me/toxicgamechannel"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="💬 Вступить в чат", 
                    url="https://t.me/toxicchati"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🎯 Играть и зарабатывать!", 
                    url="https://t.me/Toxicgmbot/toxicgameapp"  # Твоя ссылка на мини-апп
                ),
            ]
        ]
    )
    
    await message.answer(text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

async def main():
    print("🤖 Бот Toxic Game запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())












































































