import os
import json
from telegram import Bot
from flask import request
from helpers.user_helper import get_user_by_telegram_id
from helpers.telegram_helper import create_telegram, get_telegram_by_id

def get_bot():
    bot = Bot(os.environ.get("MASWOWO_BOT_TOKEN"))
    return bot

def hello_world():
    return "Hello, World!"

def start(update):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_user_by_telegram_id(update["message"]["from"]["id"])
            message = f"Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n/help\n/concert"
            bot.send_message(chat_id=update["message"]["from"]["id"], text=message)
        except:
            try:
                res = get_telegram_by_telegram_id(update["message"]["from"]["id"])
            except:
                body = {}
                body["otp"] = update
                body["chat_id"] = update["message"]["chat"]["id"]
                body["telegram_id"] = update["message"]["from"]["id"]
                res = create_telegram(body)
            
            message = f"Welcome {update["message"]["from"]["username"]} My name is Wowo and I will be your helper bot. I need to validate who you are, so please enter this code {res["otp"]} when you login/register using your nottiketcom account.\nAccess your account here https://nottiketcom.xyz/login"
            bot.send_message(chat_id=update["message"]["from"]["id"], text=message)
    except Exception as ex:
        print(ex)

def help_(update):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_user_by_telegram_id(update["message"]["from"]["id"])
            message = f"Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n/help\n/concert"
            bot.send_message(chat_id=update["message"]["from"]["id"], text=message)
        except:
            message = f"Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration"
            bot.send_message(chat_id=update["message"]["from"]["id"], text=message)
    except Exception as ex:
        print(ex)
    

def bot_start():
    update = request.get_json()
    received_message = update["message"]["text"]
    switcher = {
        "/start": start,
        "/help": help_
    }
    func = switcher.get(received_message, lambda: "Invalid month")
    func(update)
    return "Message sent!"