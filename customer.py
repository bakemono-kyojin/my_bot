from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler
import sqlite3

def customer_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        ["📦 View products"],
        ["🔙 Back"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard)
    update.message.reply_text('Customer menu:', reply_markup=reply_markup)

def view_products(update: Update, context: CallbackContext) -> None:
    # Code to view products. This will need to be handled as a conversation.
    pass

def handle_customer(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    if query.data == 'view_products':
        view_products(update, context)

