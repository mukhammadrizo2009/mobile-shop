from telegram import Update , ReplyKeyboardMarkup , KeyboardButton
from telegram.ext import CallbackContext

def order_uz(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Buyurtmalar hali bo'sh!😑\nBuyurtma berishingizni kutayabmiz!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Orqaga qaytish ⏪") , KeyboardButton("Dasturni to'xtatish!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def order_en(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Orders are still empty!😑\nWe are waiting for your order!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Come Back ⏪") , KeyboardButton("Stop the program!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )
    
def order_ru(update: Update , context: CallbackContext):
    bot = context.bot
    user = update._effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Заказы пока пусты!😑\nМы ждем вашего заказа!😊",
        reply_markup = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Возвращаться ⏪") , KeyboardButton("Остановить программу!🤔")]
            ],
            one_time_keyboard=True,
            resize_keyboard=True
        )
    )