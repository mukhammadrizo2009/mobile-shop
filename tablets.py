from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def tablet_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Planshetlar 📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple 🍏")],
                [KeyboardButton("Samsung 📱")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def samsung_tablet_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung Planshetlari📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy Tab 4")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def apple_tablet_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Apple Planshetlari📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("IPad Pro")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def tablet_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Tablets page 📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple ✨")],
                [KeyboardButton("Samsung 🪶")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def samsung_tablet_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung Tablets📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy Tab 3")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def apple_tablet_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Apple Tablets📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("IPad Max")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def tablet_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Планшеты листы 📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple 📟")],
                [KeyboardButton("Samsung 🤖")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def samsung_tablet_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung Планшеты📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy Tab 2")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def apple_tablet_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Apple Планшеты📟",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("IPad Mini")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]   
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )