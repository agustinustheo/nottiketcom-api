import os
import json
from telegram import Bot
from flask import request
from helpers.id_helper import generate_id
from helpers.cart_helper import create_cart
from helpers.user_helper import get_user_by_telegram_id
from helpers.telegram_helper import create_telegram, get_telegram_by_telegram_id
from helpers.concert_helper import get_all_concerts, get_concert_by_tags, get_concert_by_artist, get_concert_by_id

def get_bot():
    bot = Bot(os.environ.get("MASWOWO_BOT_TOKEN"))
    return bot

def hello_world():
    return "Hello, World!"

def send_otp_confirmation(chat_id):
    try:
        res = {}
        bot = get_bot()
        message = f'You have been authenticated! Hi there! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n'
        message += '/start - Authenticate user with a telegram profile\n'
        message += '/concerts - Looks up all the recent concerts available\n'
        message += '/concert_by_tags - Search for concerts by tags\n'
        message += '/concert_by_artist - Search for concerts by artist name\n'
        message += '/order - Add concert to cart by concert Id\n'
        message += '/help - Shows the entire command list for the bot\n'
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as ex:
        print(ex)

def send_checkout_confirmation(chat_id, concert_id, checkout_id):
    try:
        res = {}
        bot = get_bot()
        message = f'Concert number {concert_id} has successfully been purchased! Ticket details can be seen here https://nottiketcom.xyz/tiket/{checkout_id}\n'
        message += f'Thank you for trusting us, we hope you will enjoy the concert!'
        bot.send_message(chat_id=chat_id, text=message)
    except Exception as ex:
        print(ex)

def start(update):
    try:
        res = {}
        bot = get_bot()
        try:
            res = get_user_by_telegram_id(update["message"]["from"]["id"])
            message = f'Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n'
            message += '/start - Authenticate user with a telegram profile\n'
            message += '/concerts - Looks up all the recent concerts available\n'
            message += '/concert_by_tags - Search for concerts by tags\n'
            message += '/concert_by_artist - Search for concerts by artist name\n'
            message += '/order - Add concert to cart by concert Id\n'
            message += '/help - Shows the entire command list for the bot\n'
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
            message = f'Welcome back {res["username"]}, glad to see you! My name is Wowo and I will be your helper bot. I can help you find concert tickets if you want? You an also command me to do some other stuff using these commands:\n\n'
            message += '/start - Authenticate user with a telegram profile\n'
            message += '/concerts - Looks up all the recent concerts available\n'
            message += '/concert_by_tags - Search for concerts by tags\n'
            message += '/concert_by_artist - Search for concerts by artist name\n'
            message += '/order - Add concert to cart by concert Id\n'
            message += '/help - Shows the entire command list for the bot\n'
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
        bot = get_bot()
        try:
            if len(args) > 0:
                res = []
                user_data = get_user_by_telegram_id(update["message"]["from"]["id"])
                for x in args:
                    body = {}
                    body["name"] = user_data["username"]
                    body["email"] = user_data["email"]
                    body["cart"] = get_concert_by_id(x)
                    res.append(create_cart(body))
                message = f'You ordered {len(res)} concerts and it has been added to your cart\n'
                for idx, x in enumerate(res):
                    message+= f'\n{idx+1}. Order Id: {x["id"]}\n'
                    message+= f'    Url:    https://nottiketcom.xyz/cart/{x["id"]}\n'
                bot.send_message(chat_id=update["message"]["chat"]["id"], text=message)
            else:
                message = f'Please tell me which concert you want to watch, just give me the Id\n'
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
    received_message = received_message.split()
    case = received_message[0]
    args = received_message[1:]
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