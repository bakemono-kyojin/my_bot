from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
TELEGRAM_ADMIN_ID = os.getenv("TELEGRAM_ADMIN_ID")

def is_admin(update: Update, context: CallbackContext) -> bool:
    return update.message.from_user.id == int(TELEGRAM_ADMIN_ID)

def admin_menu(update: Update, context: CallbackContext) -> None:
    if not is_admin(update, context):
        update.message.reply_text("You are not authorized to access this.")
        return

    keyboard = [
        ["📦 Add product", "✏️ Edit product", "🗑️ Delete product"],
        ["🔙 Back"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Admin menu:', reply_markup=reply_markup)

def add_product(update: Update, context: CallbackContext) -> None:
    if not is_admin(update, context):
        update.message.reply_text("You are not authorized to access this.")
        return

    # Code to add a product. This will need to be handled as a conversation.
    pass

def edit_product(update: Update, context: CallbackContext) -> None:
    if not is_admin(update, context):
        update.message.reply_text("You are not authorized to access this.")
        return

    # Code to edit a product. This will need to be handled as a conversation.
    pass

def delete_product(update: Update, context: CallbackContext) -> None:
    if not is_admin(update, context):
        update.message.reply_text("You are not authorized to access this.")
        return

    # Code to delete a product. This will need to be handled as a conversation.
    pass

def handle_admin(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'add_product':
        add_product(update, context)
    elif query.data == 'edit_product':
        edit_product(update, context)
    elif query.data == 'delete_product':
        delete_product(update, context)

