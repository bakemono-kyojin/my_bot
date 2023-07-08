import logging
from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class AddProduct(StatesGroup):
    waiting_for_name = State()
    waiting_for_price = State()
    waiting_for_category = State()
    waiting_for_image = State()

class EditProduct(StatesGroup):
    waiting_for_id = State()
    waiting_for_name = State()
    waiting_for_price = State()
    waiting_for_category = State()
    waiting_for_image = State()

class RemoveProduct(StatesGroup):
    waiting_for_id = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    # default commands
    commands = ["/products", "/cart", "/faq", "/about_us"]
    if message.from_user.id == ADMIN_ID:
        # admin commands
        commands += ["/admin"]
    keyboard_markup.add(*(types.KeyboardButton(text) for text in commands))
    await message.reply("Hello!", reply_markup=keyboard_markup)

@dp.message_handler(commands=['admin'], user_id=ADMIN_ID, state="*")
async def admin_command(message: types.Message, state: FSMContext):
    keyboard_markup = types.ReplyKeyboardMarkup(row_width=3)
    commands = ["/add_product", "/edit_product", "/remove_product"]
    keyboard_markup.add(*(types.KeyboardButton(text) for text in commands))
    await message.reply("Admin Menu", reply_markup=keyboard_markup)

@dp.message_handler(commands=['faq'])
async def faq_command(message: types.Message):
    await message.reply("FAQ\n\n1. Question 1\nAnswer 1\n\n2. Question 2\nAnswer 2\n\n...")

@dp.message_handler(commands=['about_us'])
async def about_us_command(message: types.Message):
    await message.reply("About Us\n\nThis is some information about our shop.")

@dp.message_handler(commands=['add_product'], user_id=ADMIN_ID, state="*")
async def add_product_command(message: types.Message, state: FSMContext):
    await message.reply("Please provide the product name.")
    await AddProduct.waiting_for_name.set()

@dp.message_handler(state=AddProduct.waiting_for_name)
async def add_product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply("Please provide the product price.")
    await AddProduct.waiting_for_price.set()

@dp.message_handler(state=AddProduct.waiting_for_price)
async def add_product_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.reply("Please provide the product category.")
    await AddProduct.waiting_for_category.set()

@dp.message_handler(state=AddProduct.waiting_for_category)
async def add_product_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.reply("Please provide the product image.")
    await AddProduct.waiting_for_image.set()

@dp.message_handler(content_types=types.ContentType.PHOTO, state=AddProduct.waiting_for_image)
async def add_product_image(message: types.Message, state: FSMContext):
    await bot.download_file_by_id(message.photo[-1].file_id, destination=f'images/{message.photo[-1].file_unique_id}.jpg')
    user_data = await state.get_data()
    add_product(user_data['name'], user_data['price'], user_data['category'], f'{message.photo[-1].file_unique_id}.jpg')
    await message.reply("Product added.")
    await state.finish()

@dp.message_handler(commands=['edit_product'], user_id=ADMIN_ID, state="*")
async def edit_product_command(message: types.Message, state: FSMContext):
    await message.reply("Please provide the product ID.")
    await EditProduct.waiting_for_id.set()

@dp.message_handler(state=EditProduct.waiting_for_id)
async def edit_product_id(message: types.Message, state: FSMContext):
    await state.update_data(id=message.text)
    await message.reply("Please provide the new product name.")
    await EditProduct.waiting_for_name.set()

@dp.message_handler(state=EditProduct.waiting_for_name)
async def edit_product_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply("Please provide the new product price.")
    await EditProduct.waiting_for_price.set()

@dp.message_handler(state=EditProduct.waiting_for_price)
async def edit_product_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.reply("Please provide the new product category.")
    await EditProduct.waiting_for_category.set()

@dp.message_handler(state=EditProduct.waiting_for_category)
async def edit_product_category(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await message.reply("Please provide the new product image.")
    await EditProduct.waiting_for_image.set()

@dp.message_handler(content_types=types.ContentType.PHOTO, state=EditProduct.waiting_for_image)
async def edit_product_image(message: types.Message, state: FSMContext):
    await bot.download_file_by_id(message.photo[-1].file_id, destination=f'images/{message.photo[-1].file_unique_id}.jpg')
 user_data = await state.get_data()
    edit_product(user_data['id'], user_data['name'], user_data['price'], user_data['category'], f'{message.photo[-1].file_unique_id}.jpg')
    await message.reply("Product edited.")
    await state.finish()

@dp.message_handler(commands=['remove_product'], user_id=ADMIN_ID, state="*")
async def remove_product_command(message: types.Message, state: FSMContext):
    await message.reply("Please provide the product ID.")
    await RemoveProduct.waiting_for_id.set()

@dp.message_handler(state=RemoveProduct.waiting_for_id)
async def remove_product_id(message: types.Message, state: FSMContext):
    remove_product(message.text)
    await message.reply("Product removed.")
    await state.finish()

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
