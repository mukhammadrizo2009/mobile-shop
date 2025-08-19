from telegram import Update, InlineKeyboardMarkup , InlineKeyboardButton
from telegram.ext import CallbackContext

def start(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
    chat_id = user.id,
    text = f"Assalomu alaykum *{user.first_name}*!\n_Bizning botga xush kelibsiz!_ 😊",
    parse_mode = "markdown"
    )
    
    bot.send_message(
        chat_id = user.id,
        text = "Iltimos tillardan birini tanlang!🇺🇿\nPlease select one of the languages!🇺🇸\nПожалуйста, выберите один из языков!🇷🇺",
        reply_markup = InlineKeyboardMarkup(
            inline_keyboard = [
                [InlineKeyboardButton("Uzbek 🇺🇿" , callback_data="uz")],
                [InlineKeyboardButton("English 🇺🇸" , callback_data="us")],
                [InlineKeyboardButton("Русский 🇷🇺" , callback_data="ru")]
            ])
    )