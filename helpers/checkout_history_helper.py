from entities.faunadb_entity import get, create, update, delete

def get_checkout_history_by_email(data):
    try:
        return get('checkout_history_by_email', data)
    except Exception as ex:
        raise ex

def create_checkout_history(data):
    try:
        return create('checkout_history', data)
    except Exception as ex:
        raise ex

def update_checkout_history(id, data):
    try:
        return update('checkout_history', id, data)
    except Exception as ex:
        raise ex

def delete_checkout_history(id):
    try:
        return delete('checkout_history', id)
    except Exception as ex:
        raise ex