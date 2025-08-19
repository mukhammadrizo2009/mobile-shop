from telegram import Update ,  ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def menu_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Ro'yhatdan o'tish yakunlandi✅ \nSahifalardan birini tanlashing mumkin!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Qurulmalar🌐") , KeyboardButton("Buyurtmalar 📦")],
                [KeyboardButton("Sozlammalar⚙️") , KeyboardButton("Fikr qoldirish✍🏻")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def to_menu_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Sahifalardan birini tanlashing mumkin!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Qurulmalar🌐") , KeyboardButton("Buyurtmalar 📦")],
                [KeyboardButton("Sozlammalar⚙️") , KeyboardButton("Fikr qoldirish✍🏻")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]  
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def menu_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Registration completed✅ \nYou can choose one of the pages!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Structures🌐") , KeyboardButton("Orders 📦")],
                [KeyboardButton("Settings⚙️") , KeyboardButton("Send Idea✍🏻")],
                [KeyboardButton("Stop the program!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def to_menu_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "You can choose one of the pages!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Structures🌐") , KeyboardButton("Orders 📦")],
                [KeyboardButton("Settings⚙️") , KeyboardButton("Send Idea✍🏻")],
                [KeyboardButton("Stop the program!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def menu_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Регистрация завершена ✅ \nВы можете выбрать одну из страниц!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Структуры🌐") , KeyboardButton("Заказы 📦")],
                [KeyboardButton("Настройки⚙️") , KeyboardButton("Отправить идею✍🏻")],
                [KeyboardButton("Остановить программу!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def to_menu_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Вы можете выбрать одну из страниц!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Структуры🌐") , KeyboardButton("Заказы 📦")],
                [KeyboardButton("Настройки⚙️") , KeyboardButton("Отправить идею✍🏻")],
                [KeyboardButton("Остановить программу!🤔")]  
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def uz_menu(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Til o'zgartirildi✅ \nSahifalardan birini tanlashing mumkin!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Qurulmalar🌐") , KeyboardButton("Buyurtmalar 📦")],
                [KeyboardButton("Sozlammalar⚙️") , KeyboardButton("Fikr qoldirish✍🏻")],
                [KeyboardButton("Dasturni to'xtatish!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def en_menu(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "The language has been changed✅ \nYou can choose one of the pages!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Structures🌐") , KeyboardButton("Orders 📦")],
                [KeyboardButton("Settings⚙️") , KeyboardButton("Send Idea✍🏻")],
                [KeyboardButton("Stop the program!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def ru_menu(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id ,
        text = "Язык был изменен✅ \nВы можете выбрать одну из страниц!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Структуры🌐") , KeyboardButton("Заказы 📦")],
                [KeyboardButton("Настройки⚙️") , KeyboardButton("Отправить идею✍🏻")],
                [KeyboardButton("Остановить программу!🤔")]   
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )