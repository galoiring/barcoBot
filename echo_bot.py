import logging

import telebot

bot_token = "5951730571:AAFJjGmdBUKse_a-si3n9Ia6yDDULroR0QM"
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(content_types=['photo'])
def heandle_photos(message):
    bot.reply_to(message, "This is a message handler")
    bot.send_photo(message.chat.id, message.photo[0])


# # Handles all sent photo files
# @bot.message_handler(content_types=['photo'])
# def handle_docs_audio(message):
#     logging.warning(message)
#
#     bot.send_chat_action(message, 'typing')
#     # bot.send_photo(message.id, message.photo)
#

bot.infinity_polling()
