from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def about_english_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Uzur bizda hozircha Ingliz tili ishlamaydi!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_russian_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Uzur bizda hozircha Rus tili ishlamaydi!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def about_phone_number_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Raqam o'zgartirildi!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_uzbek_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Sorry, the Uzbek language does not work for us at the moment!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_russian_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Sorry, we don't have Russian at the moment!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_phone_number_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "The number has been changed!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def about_uzbek_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "К сожалению, узбекский язык у нас в данный момент не работает!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_english_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Извините, на данный момент у нас нет английского языка!😥",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def about_phone_number_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Номер был изменен!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )  