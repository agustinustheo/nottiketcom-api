from flask import Flask
app = Flask(__name__)

from services.index import hello_world
app.add_url_rule('/', methods=['GET'],  view_func=hello_world)

from services.user_service import get_user_by_email, get_user_by_telegram_id, get_user_by_username, login_user, create_user, update_user, delete_user
app.add_url_rule('/user/update', methods=['PUT'],  view_func=update_user)
app.add_url_rule('/user/login', methods=['POST'],  view_func=login_user)
app.add_url_rule('/user/create', methods=['POST'],  view_func=create_user)
app.add_url_rule('/user/delete', methods=['DELETE'],  view_func=delete_user)
app.add_url_rule('/user/email', methods=['POST'],  view_func=get_user_by_email)
app.add_url_rule('/user/username', methods=['POST'],  view_func=get_user_by_username)
app.add_url_rule('/user/telegram/id', methods=['POST'],  view_func=get_user_by_telegram_id)

from services.telegram_service import get_telegram_by_otp, create_telegram, update_telegram, delete_telegram
app.add_url_rule('/telegram/otp', methods=['POST'],  view_func=get_telegram_by_otp)
app.add_url_rule('/telegram/update', methods=['PUT'],  view_func=update_telegram)
app.add_url_rule('/telegram/create', methods=['POST'],  view_func=create_telegram)
app.add_url_rule('/telegram/delete', methods=['DELETE'],  view_func=delete_telegram)

from services.checkout_history_service import get_checkout_history_by_email, create_checkout_history, update_checkout_history, delete_checkout_history
app.add_url_rule('/checkout/history/update', methods=['PUT'],  view_func=update_checkout_history)
app.add_url_rule('/checkout/history/create', methods=['POST'],  view_func=create_checkout_history)
app.add_url_rule('/checkout/history/delete', methods=['DELETE'],  view_func=delete_checkout_history)
app.add_url_rule('/checkout/history/email', methods=['POST'],  view_func=get_checkout_history_by_email)

from services.concert_service import get_all_concerts, get_concert_by_artist, get_concert_by_price, get_concert_by_tags, create_concert, update_concert, delete_concert
app.add_url_rule('/concert', methods=['POST'],  view_func=get_all_concerts)
app.add_url_rule('/concert/update', methods=['PUT'],  view_func=update_concert)
app.add_url_rule('/concert/create', methods=['POST'],  view_func=create_concert)
app.add_url_rule('/concert/delete', methods=['DELETE'],  view_func=delete_concert)
app.add_url_rule('/concert/tag', methods=['POST'],  view_func=get_concert_by_tags)
app.add_url_rule('/concert/price', methods=['POST'],  view_func=get_concert_by_price)
app.add_url_rule('/concert/artist', methods=['POST'],  view_func=get_concert_by_artist)