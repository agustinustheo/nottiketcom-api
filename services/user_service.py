import base64
from flask import request, jsonify
from helpers.bcrypt_helper import hash_password, check_password
from helpers import user_helper, telegram_helper

def otp_user():
    try:
        req_data = request.get_json()
        otp = base64.b64decode(request.headers['Authorization'].split()[1].encode('ascii')).decode('ascii')
        t_res = telegram_helper.get_telegram_by_otp(otp)
        user_res = user_helper.update_user(req_data["id"], t_res)
        telegram_helper.delete_telegram(t_res["id"], t_res)
        return jsonify(user_res)
    except Exception as ex:
        raise ex

def login_user():
    try:
        email, password = base64.b64decode(request.headers['Authorization'].split()[1].encode('ascii')).decode('ascii').split(":")
        res = user_helper.get_user_by_email(email)
        if check_password(password, res["password"]):
            return jsonify({"login_status": True, "user_id": res["id"]})
        return jsonify({"login_status": False})
    except Exception as ex:
        raise ex

def get_user_by_id():
    try:
        req_data = request.get_json()
        return jsonify(user_helper.get_user_by_id(req_data["id"]))
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