from entities.faunadb_entity import get, create, update, delete

def get_user_by_email(data):
    try:
        return get('user_by_email', data)
    except Exception as ex:
        raise ex

def get_user_by_telegram_id(data):
    try:
        return get('user_by_telegram_id', data)
    except Exception as ex:
        raise ex

def get_user_by_username(data):
    try:
        return get('user_by_username', data)
    except Exception as ex:
        raise ex

def get_user_by_id(id):
    try:
        return get_by_id('users', id)
    except Exception as ex:
        raise ex

def create_user(data):
    try:
        return create('users', data)
    except Exception as ex:
        raise ex

def update_user(id, data):
    try:
        return update('users', id, data)
    except Exception as ex:
        raise ex

def delete_user(id):
    try:
        return delete('users', id)
    except Exception as ex:
        raise ex