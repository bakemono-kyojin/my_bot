from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")

# Initialize bot and dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton("🛒 Products", callback_data='products'),
        types.InlineKeyboardButton("🚚 Delivery Info", callback_data='delivery_info'),
        types.InlineKeyboardButton("❓ FAQ", callback_data='faq'),
        types.InlineKeyboardButton("🛍️ Cart (0)", callback_data='cart'),
    ]
    
    if message.from_user.id == int(TELEGRAM_ADMIN_ID):
        buttons.append(types.InlineKeyboardButton("💼 Admin", callback_data='admin'))
    
    keyboard.add(*buttons)

    await message.reply('Hello! Welcome to our shop. How can I assist you today?', reply_markup=keyboard)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
