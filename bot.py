from telegram import *
from telegram.ext import *
TOKEN = '5242658033:AAGf9oBPlH1R5rqHzl_V70zhsU8nidxX_E0'

def start(update: Update, context: CallbackContext):
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.effective_chat.id}")

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()