import os
from telegram import Bot
from flask import request, jsonify

def get_bot():
    bot = Bot(os.environ.get("BOT_TOKEN"))
    return bot

def hello_world():
    return 'Hello, World!'

def hi():
    update = request.get_json()
    bot.send_message(chat_id=update['message']['chat']['id'], text=jsonify(update))