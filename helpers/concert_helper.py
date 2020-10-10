from entities.faunadb_entity import get, get_by_index, create, update, delete

def get_all_concerts():
    try:
        return get_by_index('all_concerts')
    except Exception as ex:
        raise ex

def get_concert_by_artist(data):
    try:
        return get('concert_by_artist', data)
    except Exception as ex:
        raise ex

def get_concert_by_price(data):
    try:
        return get('concert_by_price', data)
    except Exception as ex:
        raise ex

def get_concert_by_tags(data):
    try:
        return get('concert_by_tags', data)
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