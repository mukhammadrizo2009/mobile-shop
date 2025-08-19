from telegram import Update , ReplyKeyboardRemove , ReplyKeyboardMarkup
from telegram.ext import CallbackContext

def stop(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    
    context.user_data["stopped"] = True
    
    bot.send_message(
        chat_id=user.id,
        text="Dastur yakunlandi!😑\nThe program has ended!😑\nПрограмма завершилась!😑",
        reply_markup=ReplyKeyboardRemove()
    )
  