from telegram import Update ,  ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def location_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Manzilni yuboring!🗺️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Manzil yuborish!ℹ️" , request_location=True)],
                [KeyboardButton("O'tkazib yuborish!⏩")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
def location_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Submit the address!🗺️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Send address!ℹ️" , request_location=True)],
                [KeyboardButton("Skipping!⏩")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def location_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Отправьте адрес!🗺️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Отправить адрес!ℹ️" , request_location=True)],
                [KeyboardButton("Пропуск!⏩")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )