from flask import request, jsonify
from helpers import checkout_history_helper

def get_checkout_history_by_email():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.get_checkout_history_by_email(req_data["email"]))
    except Exception as ex:
        raise ex

def create_checkout_history():
    try:
        req_data = request.get_json()
        return jsonify(checkout_history_helper.create_checkout_history(req_data))
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