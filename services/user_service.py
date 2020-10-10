import base64
from flask import request, jsonify
from helpers.bcrypt_helper import hash_password, check_password
from helpers import user_helper

def get_user_by_email():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.get_user_by_email(req_data["email"]))
    except Exception as ex:
        raise ex

def login_user():
    try:
        email, password = base64.b64decode(request.headers['Authorization'].split()[1].encode('ascii')).decode('ascii').split(":")
        res = user_helper.get_user_by_email(email)
        if check_password(password, res["password"]):
            return jsonify({"login_status": True})
        return jsonify({"login_status": False})
    except Exception as ex:
        raise ex

def get_user_by_telegram_id():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.get_user_by_telegram_id(req_data["telegram_id"]))
    except Exception as ex:
        raise ex

def get_user_by_username():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.get_user_by_username(req_data["username"]))
    except Exception as ex:
        raise ex

def create_user():
    try:
        email, password = base64.b64decode(request.headers['Authorization'].split()[1].encode('ascii')).decode('ascii').split(":")
        req_data = request.get_json()
        req_data["email"] = email
        req_data["password"] = hash_password(password)
        return jsonify(user_helper.create_user(req_data))
    except Exception as ex:
        raise ex

def update_user():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.update_user(req_data["id"], req_data["data"]))
    except Exception as ex:
        raise ex

def delete_user():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.delete_user(req_data["id"]))
    except Exception as ex:
        raise ex