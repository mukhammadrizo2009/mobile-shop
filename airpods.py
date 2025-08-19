from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def airpods_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Quloqchinlar 🎧",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Air Pods Max 🎧")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def airpods_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Air Podses 🎧",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Air Pods Pro 🎧")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def airpods_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Наушники 🎧 ",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Air Pods Pro 5 🎧")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )