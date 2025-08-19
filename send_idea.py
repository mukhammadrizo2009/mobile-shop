from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def send_idea_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Fikringizni yozib yuboring!⬇️\nmuhammadrizomirzaev671@gmail.com",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def send_idea_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Write your opinion!⬇️\nmuhammadrizomirzaev671@gmail.com",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def send_idea_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Напишите свое мнение!⬇️\nmuhammadrizomirzaev671@gmail.com",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )