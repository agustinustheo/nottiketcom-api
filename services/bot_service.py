import os
import json
from telegram import Bot
from flask import request

def get_bot():
    bot = Bot(os.environ.get("MASWOWO_BOT_TOKEN"))
    return bot

def hello_world():
    return 'Hello, World!'

def hi():
    update = request.get_json()
    bot = get_bot()
    bot.send_message(chat_id=update['message']['chat']['id'], text=json.dumps(update))