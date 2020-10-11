from flask import request, jsonify
from services.bot_service import send_checkout_confirmation
from helpers import checkout_history_helper, cart_helper, user_helper

def get_checkout_history_by_email():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.get_checkout_history_by_email(req_data["email"]))
    except Exception as ex:
        raise ex

def get_checkout_history_by_id():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.get_checkout_history_by_id(req_data["id"]))
    except Exception as ex:
        raise ex

def create_checkout_history():
    try:
        req_data = request.get_json()
        res = cart_helper.get_cart_by_id(req_data["id"])
        res["cart_id"] = res["id"]
        res.pop('id', None)

        cart_helper.delete_cart(res["cart_id"])

        chat_id = user_helper.get_user_by_email(res["email"])["chat_id"]
        concert_id = res["cart"]["id"]
        checkout = checkout_history_helper.create_checkout_history(res)
        send_checkout_confirmation(chat_id, concert_id, checkout["id"])
        return jsonify(checkout)
    except Exception as ex:
        raise ex

def update_checkout_history():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.update_checkout_history(req_data["id"], req_data["data"]))
    except Exception as ex:
        raise ex

def delete_checkout_history():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.delete_checkout_history(req_data["id"]))
    except Exception as ex:
        raise ex