import telegram
from telegram import *
from telegram.ext import *
TOKEN = '5242658033:AAGf9oBPlH1R5rqHzl_V70zhsU8nidxX_E0'

# creating some basic functions for the bot
def start(update: Update, context: CallbackContext):
    # Two methods to do this
    #1
    #update.message.reply_text(f'Hello {update.effective_user.first_name}')
    #2
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Chat connected!\nName: {update.effective_user.full_name}\nUsername: {update.effective_user.username}")

"""def sticker(update: Update, context: CallbackContext):
    context.bot.send_sticker("Stickers/3005.webp",'Sticker')"""

def button(update: Update, context: CallbackContext):
    button  = InlineKeyboardMarkup([
        [InlineKeyboardButton("Male",callback_data="Male")],[InlineKeyboardButton("Female",callback_data="Female")],
        [InlineKeyboardButton("Prefer not to say",callback_data="Prefer not to say")]
    ])

    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=button, text="Choose your gender:")
    #update.message.reply_text(button)
    #context.bot.send_message(chat_id=update.effective_chat.id,text=f"Gender updated as {}")

def keyboard(update: Update, context: CallbackContext):
    button = [
        ["Male"],["Female"],
        ["Prefer not to say"]
    ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(button), text="Choose your gender:")
    

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
#updater.dispatcher.add_handler(CommandHandler('sticker', sticker))
updater.dispatcher.add_handler(CommandHandler('button',button))
updater.dispatcher.add_handler(CommandHandler('keyboard',keyboard))

updater.start_polling()
updater.idle()