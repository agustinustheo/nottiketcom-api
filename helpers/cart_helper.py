from entities.faunadb_entity import get, get_by_id, create, update, delete

def get_cart_by_email(data):
    try:
        return get('cart_by_email', data)
    except Exception as ex:
        raise ex

def get_cart_by_id(id):
    try:
        return get_by_id('cart', id)
    except Exception as ex:
        raise ex

def create_cart(data):
    try:
        return create('cart', data)
    except Exception as ex:
        raise ex

def update_cart(id, data):
    try:
        return update('cart', id, data)
    except Exception as ex:
        raise ex

def delete_cart(id):
    try:
        return delete('cart', id)
    except Exception as ex:
        raise ex