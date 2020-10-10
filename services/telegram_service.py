from flask import request, jsonify
from helpers import telegram_helper

def get_telegram_by_otp():
    try:
        req_data = request.get_json()
        return jsonify(telegram_helper.get_telegram_by_otp(req_data["otp"]))
    except Exception as ex:
        raise ex

def create_telegram():
    try:
        req_data = request.get_json()
        return jsonify(telegram_helper.create_telegram(req_data))
    except Exception as ex:
        raise ex

def update_telegram():
    try:
        req_data = request.get_json()
        return jsonify(telegram_helper.update_telegram(req_data["id"], req_data["data"]))
    except Exception as ex:
        raise ex

def delete_telegram():
    try:
        req_data = request.get_json()
        return jsonify(telegram_helper.delete_telegram(req_data["id"]))
    except Exception as ex:
        raise ex