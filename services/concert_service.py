from flask import request, jsonify
from helpers import concert_helper

def get_all_concerts():
    try:
        return jsonify(concert_helper.get_all_concerts())
    except Exception as ex:
        raise ex

def get_concert_by_artist():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.get_concert_by_artist(req_data["artist"]))
    except Exception as ex:
        raise ex

def get_concert_by_price():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.get_concert_by_price(req_data["price"]))
    except Exception as ex:
        raise ex

def get_concert_by_tags():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.get_concert_by_tags(req_data["tags"]))
    except Exception as ex:
        raise ex

def create_concert():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.create_concert(req_data))
    except Exception as ex:
        raise ex

def update_concert():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.update_concert(req_data["id"], req_data["data"]))
    except Exception as ex:
        raise ex

def delete_concert():
    try:
        req_data = request.get_json()
        return jsonify(concert_helper.delete_concert(req_data["id"]))
    except Exception as ex:
        raise ex