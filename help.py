from telegram import Update
from telegram.ext import CallbackContext

def help(update: Update , context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    bot.send_message(
        chat_id = user.id,
        text = "Yordam uchun murojat qiling!\nAsk for help!\nПросите о помощи!\n muhammadrizomirzaev671@gmail.com"
    )