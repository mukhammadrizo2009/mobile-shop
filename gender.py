from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def gender_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Jins qabul qilindi!✅"
        )
    bot.send_message(
        chat_id = user.id ,
        text = "Telefon raqamni yuboring!📞",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Raqamni yuborish!ℹ️" , request_contact=True)],
                [KeyboardButton("Tashlab ketish! ⏩")]
        ],
        one_time_keyboard=True,
        resize_keyboard=True
        )
    )
    
def gender_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Gender accepted!✅"
        )
    bot.send_message(
        chat_id = user.id ,
        text = "Send your phone number!📞",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Send number!ℹ️" , request_contact=True)],
                [KeyboardButton("Skip! ⏩")]
        ],
        one_time_keyboard=True,
        resize_keyboard=True
        )
    )
    
def gender_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Пол принят!✅"
        )
    bot.send_message(
        chat_id = user.id ,
        text = "Отправьте свой номер телефона!📞",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Отправить номер!ℹ️" , request_contact=True)],
                [KeyboardButton("Пропускать! ⏩")]
        ],
        one_time_keyboard=True,
        resize_keyboard=True
        )
    )