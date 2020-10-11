import os
import json
from telegram import Bot
from flask import request
from helpers.id_helper import generate_id
from helpers.user_helper import get_user_by_telegram_id
from helpers.telegram_helper import create_telegram, get_telegram_by_telegram_id
from helpers.concert_helper import get_all_concerts, get_concert_by_tags, get_concert_by_artist

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
            message = f'Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n/help\n/concert'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except:
            try:
                res = get_telegram_by_telegram_id(update["message"]["from"]["id"])
            except Exception as ex:
                print(ex)

                body = {}
                body["otp"] = generate_id(6)
                body["chat_id"] = update["message"]["chat"]["id"]
                body["telegram_id"] = update["message"]["from"]["id"]
                res = create_telegram(body)
            
            message = f'Welcome {update["message"]["from"]["username"]} My name is Wowo and I will be your helper bot. I need to validate who you are, so please enter this code {res["otp"]} when you login/register using your nottiketcom account.\n\nAccess your account here https://nottiketcom.xyz/login'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)

def help_(update):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_user_by_telegram_id(update["message"]["from"]["id"])
            message = f'Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n/help\n/concert'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except Exception as ex:
            print(ex)

            message = f'Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)

def make_lines():
    lines = ""
    for x in range(10):
        lines += "-"
    return lines

def concerts(update):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_all_concerts()
            message = 'Here are all the online concerts we have this month:\n'
            for idx, x in enumerate(res):
                message+= f'\n{idx+1}. Item Id: {x["id"]}\n'
                message+= f'    Name:    {x["name"]}\n'
                message+= f'    Date:    {x["date"]}\n'
                message+= f'    Price:    {x["price"]}\n'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except Exception as ex:
            print(ex)

            message = f'Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)

def concert_by_tags(update, args):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_concert_by_tags(args)
            if(len(res) > 0):
                message = f'Here are all the online concerts tagged {str(args)} we have this month:\n'
                for idx, x in enumerate(res):
                    message+= f'\n{idx+1}. Item Id: {x["id"]}\n'
                    message+= f'    Name:    {x["name"]}\n'
                    message+= f'    Date:    {x["date"]}\n'
                    message+= f'    Price:    {x["price"]}\n'
                bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
            else:
                message = f'Sorry! We couldn\'t find any online concerts tagged {str(args)} this month\n'
                bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except Exception as ex:
            print(ex)

            message = f'Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)

def concert_by_artist(update, args):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_concert_by_artist(args)
            if(len(res) > 0):
                message = f'Here are all the online concerts by {str(args)} we have this month:\n'
                for idx, x in enumerate(res):
                    message+= f'\n{idx+1}. Item Id: {x["id"]}\n'
                    message+= f'    Name:    {x["name"]}\n'
                    message+= f'    Date:    {x["date"]}\n'
                    message+= f'    Price:    {x["price"]}\n'
                bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
            else:
                message = f'Sorry! We couldn\'t find any online concerts by {str(args)} this month\n'
                bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except Exception as ex:
            print(ex)

            message = f'Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)

def order(update, args):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_concert_by_artist(args)
            message = f'Here are all the online concerts by {str(args)} we have this month:\n'
            for idx, x in enumerate(res):
                message+= f'\n{idx+1}. Item Id: {x["id"]}\n'
                message+= f'    Name:    {x["name"]}\n'
                message+= f'    Date:    {x["date"]}\n'
                message+= f'    Price:    {x["price"]}\n'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
        except Exception as ex:
            print(ex)

            message = f'Sorry {update["message"]["from"]["username"]} you have not registered this account please chat /start to begin registration'
            bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
    except Exception as ex:
        print(ex)
    
def bot_start():
    update = request.get_json()
    received_message = update["message"]["text"]
    if len(received_message.split()) > 1:
        switch_with_args(update, received_message)
    else:
        switch_without_args(update, received_message)
    return "Message sent!"

def switch_with_args(update, received_message):
    print(received_message)
    received_message = received_message.split()
    case = received_message[0]
    args = received_message[1:]
    print(case, args)
    switcher = {
        "/order": order,
        "/concert_by_tags": concert_by_tags,
        "/concert_by_artist": concert_by_artist
    }
    func = switcher.get(case)
    if func is None:
        help_(update)
    else:
        func(update, args)

def switch_without_args(update, received_message):
    switcher = {
        "/help": help_,
        "/start": start,
        "/concerts": concerts
    }
    func = switcher.get(received_message, help_)
    func(update)