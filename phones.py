from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def phones_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Telefonlar ro'yhati!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple 🍎")],
                [KeyboardButton("Samsung ✨")],
                [KeyboardButton("Xiomi 🔮")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
                
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def iphones_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Iphone Telefonlar!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Iphone 16 Pro Max")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def samsung_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung Telefonlar!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy S25 Ultra")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def xiomi_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Xiomi telefonlar📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Xiomi 15 ultra")],
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )   
    
def phones_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Phone list!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple 🌐")],
                [KeyboardButton("Samsung 📟")],
                [KeyboardButton("Xiomi ✅")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
                
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def iphones_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Iphone phones!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Iphone 15 Pro Max")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def samsung_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung phones!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy S24 Ultra")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def xiomi_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Xiomi phones📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Xiomi 14 ultra")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )
    
def phones_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Список телефонов!",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Apple 📱")],
                [KeyboardButton("Samsung 🖐🏻")],
                [KeyboardButton("Xiomi 🤩")],
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
                
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def iphones_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Iphone телефоны!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Iphone 14 Pro Max")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def samsung_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Samsung телефоны!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Galaxy S23 Ultra")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )

def xiomi_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Xiomi телефоны!📱",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Xiomi 13 ultra")],
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            resize_keyboard=True,
            one_time_keyboard=True
        )
    )