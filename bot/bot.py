import requests
import http.client
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

def start(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Welcome to BelajarBotBot!")

def kanye(bot, update):
    response = requests.get("https://api.kanye.rest/")
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=response.json()["quote"])

def fox(bot, update):
    response = requests.get("https://randomfox.ca/floof/")
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=response.json()["image"])

def echo(bot, update):
    chat_id = update.message.chat_id
    chatbot = ChatBot('WowoBot')

    # First, lets train our bot with some data
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Get a response to the input text 'I would like to book a flight.'
    response = chatbot.get_response(update.message.text)
    if response.confidence <= 0.4:
        bot.send_message(chat_id=chat_id, text="Maaf, Wowo belum mengerti maksudmu, bolehkah diulang lagi? :(")
    else:
        bot.send_message(chat_id=chat_id, text=str(response))

def search_by_artist(bot, update, args):
    chat_id = update.message.chat_id
    try:
        artist_name = str(args[0])
        response = requests.post("https://localhost:5000/concert/artist", data={'artist': artist_name})
        bot.send_message(chat_id=chat_id, text=artist_name)
    except Exception as e:
        bot.send_message(chat_id = chat_id, text = str(e))

def main():
    updater = Updater('')
    dp = updater.dispatcher
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('whatdidkanyesay', kanye))
    dp.add_handler(CommandHandler('sendmeafox', fox))
    dp.add_handler(CommandHandler('artist', search_by_artist, pass_args= True))
    dp.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()