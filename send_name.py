from telegram import Update ,  ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def send_name_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = f"Ism familya qabul qilindi *{user.full_name}*",
        parse_mode = "markdown"
    )
    
    bot.send_message(
        chat_id = user.id ,
        text = "Jinsingizni tanlang!👨🏻👩🏻‍🦱" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Erkak 👨🏻") , KeyboardButton("Ayol 👩🏻‍🦱")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def send_name_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = f"The firstname lastname is adopted *{user.full_name}*",
        parse_mode = "markdown"
    )
    
    bot.send_message(
        chat_id = user.id ,
        text = "Choose your gender!👨🏻👩🏻‍🦱" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Men 👨🏻") , KeyboardButton("Women 👩🏻‍🦱")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def send_name_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = f"Имя фамилия принята *{user.full_name}*",
        parse_mode = "markdown"
    )
    
    bot.send_message(
        chat_id = user.id ,
        text = "Выберите свой пол!👨🏻👩🏻‍🦱" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Мужчины 👨🏻") , KeyboardButton("Женщины 👩🏻‍🦱")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )