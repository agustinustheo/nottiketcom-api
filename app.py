from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from services import bot_service
app.add_url_rule('/', methods=['GET'],  view_func=bot_service.hello_world)
app.add_url_rule('/', methods=['POST'],  view_func=bot_service.hi)

from services import user_service
app.add_url_rule('/user/update', methods=['PUT'],  view_func=user_service.update_user)
app.add_url_rule('/user/login', methods=['GET'],  view_func=user_service.login_user)
app.add_url_rule('/user/create', methods=['POST'],  view_func=user_service.create_user)
app.add_url_rule('/user/delete', methods=['DELETE'],  view_func=user_service.delete_user)
app.add_url_rule('/user/email', methods=['POST'],  view_func=user_service.get_user_by_email)
app.add_url_rule('/user/username', methods=['POST'],  view_func=user_service.get_user_by_username)
app.add_url_rule('/user/telegram/id', methods=['POST'],  view_func=user_service.get_user_by_telegram_id)

from services import telegram_service
app.add_url_rule('/telegram/otp', methods=['POST'],  view_func=telegram_service.get_telegram_by_otp)
app.add_url_rule('/telegram/update', methods=['PUT'],  view_func=telegram_service.update_telegram)
app.add_url_rule('/telegram/create', methods=['POST'],  view_func=telegram_service.create_telegram)
app.add_url_rule('/telegram/delete', methods=['DELETE'],  view_func=telegram_service.delete_telegram)

from services import cart_service
app.add_url_rule('/cart/id', methods=['POST'],  view_func=cart_service.get_cart_by_id)
app.add_url_rule('/cart/email', methods=['POST'],  view_func=cart_service.get_cart_by_email)
app.add_url_rule('/cart/update', methods=['PUT'],  view_func=cart_service.update_cart)
app.add_url_rule('/cart/create', methods=['POST'],  view_func=cart_service.create_cart)
app.add_url_rule('/cart/delete', methods=['DELETE'],  view_func=cart_service.delete_cart)

from services import checkout_history_service
app.add_url_rule('/checkout/history/id', methods=['POST'],  view_func=checkout_history_service.get_checkout_history_by_id)
app.add_url_rule('/checkout/history/email', methods=['POST'],  view_func=checkout_history_service.get_checkout_history_by_email)
app.add_url_rule('/checkout/history/update', methods=['PUT'],  view_func=checkout_history_service.update_checkout_history)
app.add_url_rule('/checkout/history/create', methods=['POST'],  view_func=checkout_history_service.create_checkout_history)
app.add_url_rule('/checkout/history/delete', methods=['DELETE'],  view_func=checkout_history_service.delete_checkout_history)

from services import concert_service
app.add_url_rule('/concert', methods=['POST'],  view_func=concert_service.get_all_concerts)
app.add_url_rule('/concert/update', methods=['PUT'],  view_func=concert_service.update_concert)
app.add_url_rule('/concert/create', methods=['POST'],  view_func=concert_service.create_concert)
app.add_url_rule('/concert/delete', methods=['DELETE'],  view_func=concert_service.delete_concert)
app.add_url_rule('/concert/id', methods=['POST'],  view_func=concert_service.get_concert_by_tags)
app.add_url_rule('/concert/tag', methods=['POST'],  view_func=concert_service.get_concert_by_tags)
app.add_url_rule('/concert/price', methods=['POST'],  view_func=concert_service.get_concert_by_price)
app.add_url_rule('/concert/artist', methods=['POST'],  view_func=concert_service.get_concert_by_artist)