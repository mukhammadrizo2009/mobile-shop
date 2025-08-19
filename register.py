from telegram import Update, ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext




def register_uz(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user

    context.user_data['lang'] = 'uz'
    
    bot.send_message(
        chat_id = user.id ,
        text = "Siz O'zbek tilini tanladingiz!🇺🇿\nRoyhatdan o'tish boshlandi!🏁"
    )
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "Ism familyangiz yuboring!⌨️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Ma'lumotni yuborish!🪪")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    

def register_en(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update.effective_user
    
    context.user_data['lang'] = 'us'
    
    bot.send_message(
        chat_id = user.id ,
        text = "You have selected English!🇺🇸\nRegistration has begun!🏁"
    )
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "Send your firstname and lastname!⌨️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Submit information!🪪")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    

def register_ru(update: Update , context: CallbackContext) -> None:
    bot = context.bot
    user = update._effective_user

    context.user_data['lang'] = 'ru'
    
    bot.send_message(
        chat_id = user.id ,
        text = "Вы выбрали русский!🇷🇺\nРегистрация началась!🏁"
    )
    
    update.callback_query.message.delete()
    
    bot.send_message(
        chat_id = user.id ,
        text = "Отправьте свое имя и фамилию!⌨️",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Отправить информацию!🪪")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )