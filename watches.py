from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def watches_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Smart Watchlar ⌚",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mi Band 6")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def watches_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Smart Watches ⌚",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mi Band 5")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def watches_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Умные часы  ⌚",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Mi Band 9")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )