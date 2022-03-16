from telegram import *
from telegram.ext import *
TOKEN = '5242658033:AAGf9oBPlH1R5rqHzl_V70zhsU8nidxX_E0'

# creating some basic functions for the bot
def start(update: Update, context: CallbackContext):
    # Two methods to do this
    #1. update.message.reply_text(f'Hello {update.effective_user.first_name}')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.effective_chat.id}") #2

def sticker(update: Update, context: CallbackContext):
    context.bot.send_sticker("/stickers/3005.webp",'Sticker')


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('sticker', sticker))

updater.start_polling()
updater.idle()