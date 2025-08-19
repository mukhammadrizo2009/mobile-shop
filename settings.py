from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def settings_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Sozlammalar ochildi!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tilni o'zgartirish!🔃") , KeyboardButton("Telfon raqamni o'zgartirish!")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        
    )

def change_language_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Tilni tanlang!🌐",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Ingliz 🇺🇸") , KeyboardButton("Rus 🇷🇺")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def change_phone_number_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Yangi raqamni yuboring!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Raqamni o'zgartirish!")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def settings_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Settings opened!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Change the language!🔃") , KeyboardButton("Change phone number!")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        
    )

def change_language_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Select a language!🌐",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Uzbek 🇺🇿") , KeyboardButton("Russian 🇷🇺")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def change_phone_number_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Send a new number!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Change number!")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def settings_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Настройки открыты!🫡",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Изменить язык!🔃") , KeyboardButton("Изменить номер телефона!")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
        
    )

def change_language_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Выберите язык!🌐",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Английский 🇺🇸") , KeyboardButton("Узбекский 🇺🇿")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def change_phone_number_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Отправить новый номер!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Изменить номер!")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )