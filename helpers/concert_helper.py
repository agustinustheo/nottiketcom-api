from entities.faunadb_entity import get, get_multiple, get_by_id, create, update, delete

def get_all_concerts():
    try:
        return get_multiple('all_concerts')
    except Exception as ex:
        raise ex

def get_concert_by_id(id):
    try:
        return get_by_id('concerts', id)
    except Exception as ex:
        raise ex

def get_concert_by_artist(data):
    try:
        return get_multiple('concert_by_artist', data)
    except Exception as ex:
        raise ex

def get_concert_by_price(data):
    try:
        return get('concert_by_price', data)
    except Exception as ex:
        raise ex

def get_concert_by_tags(data):
    try:
        return get_multiple('concert_by_tags', data)
    except Exception as ex:
        raise ex

def create_concert(data):
    try:
        return create('concerts', data)
    except Exception as ex:
        raise ex

def update_concert(id, data):
    try:
        return update('concerts', id, data)
    except Exception as ex:
        raise ex

def delete_concert(id):
    try:
        return delete('concerts', id)
    except Exception as ex:
        raise ex