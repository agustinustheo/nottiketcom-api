from flask import request, jsonify
from helpers import cart_helper

def get_cart_by_email():
    try:
        req_data = request.get_json()
        return jsonify(cart_helper.get_cart_by_email(req_data["email"]))
    except Exception as ex:
        raise ex

def get_cart_by_id():
    try:
        req_data = request.get_json()
        return jsonify(cart_helper.get_cart_by_id(req_data["id"]))
    except Exception as ex:
        raise ex

def create_cart():
    try:
        req_data = request.get_json()
        return jsonify(cart_helper.create_cart(req_data))
    except Exception as ex:
        raise ex

def update_cart():
    try:
        req_data = request.get_json()
        return jsonify(cart_helper.update_cart(req_data["id"], req_data["data"]))
    except Exception as ex:
        raise ex

def delete_cart():
    try:
        req_data = request.get_json()
        return jsonify(cart_helper.delete_cart(req_data["id"]))
    except Exception as ex:
        raise ex