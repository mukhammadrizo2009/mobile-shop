from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def menu_desktops_uz(update: Update , context: CallbackContext):
    bot = context.bot 
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Qurulmalar sahifasi!" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Telefonlar 📱") , KeyboardButton("Planshetlar 📟")],
                [KeyboardButton("Smart Watchlar ⌚") , KeyboardButton("Quloqchinlar 🎧")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )

def menu_desktops_en(update: Update , context: CallbackContext):
    bot = context.bot 
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Devices page!" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Phones 📱") , KeyboardButton("Tablets 📟")],
                [KeyboardButton("Smart Watches ⌚") , KeyboardButton("Air Pods 🎧")],
                [KeyboardButton("Go Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def menu_desktops_ru(update: Update , context: CallbackContext):
    bot = context.bot 
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Страница устройств!" ,
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Телефоны 📱") , KeyboardButton("Планшеты 📟")],
                [KeyboardButton("Умные часы ⌚") , KeyboardButton("Наушники 🎧")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )