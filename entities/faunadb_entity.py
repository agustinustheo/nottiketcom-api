import os
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

def get_multiple(index, data=None):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        res_arr = []
        if data is None:
            res = serverClient.query(   
                q.map_(
                    q.lambda_("data", q.get(q.var("data"))), 
                    q.paginate(q.match(q.index(index)))
                )
            )
            res_arr.extend(res["data"])
        elif isinstance(data, list):
            for x in data:
                res = serverClient.query(   
                    q.map_(
                        q.lambda_("data", q.get(q.var("data"))), 
                        q.paginate(q.match(q.index(index), x))
                    )
                )
                res_arr.extend(res["data"])
        else:
            res = serverClient.query(   
                q.map_(
                    q.lambda_("data", q.get(q.var("data"))), 
                    q.paginate(q.match(q.index(index), data))
                )
            )
            res_arr.extend(res["data"])

        arr = []
        for x in res_arr:
            x["data"]["id"] = x["ref"].id()
            arr.append(x["data"])
        return arr
    except Exception as ex:
        raise ex

def get(index, data):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        res = serverClient.query(q.get(q.match(q.index(index), data)))
        res["data"]["id"] = res["ref"].id()
        return res["data"]
    except Exception as ex:
        raise ex

def get_by_id(collection, id):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        res = serverClient.query(q.get(q.ref(q.collection(collection), id)))
        res["data"]["id"] = res["ref"].id()
        return res["data"]
    except Exception as ex:
        raise ex

def create(collection, data):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        res = serverClient.query(q.create(q.collection(collection), {"data": data}))
        res["data"]["id"] = res["ref"].id()
        return res["data"]
    except Exception as ex:
        raise ex

def update(collection, id, data):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        res = serverClient.query(q.update(q.ref(q.collection(collection), id), {"data": data}))
        res["data"]["id"] = res["ref"].id()
        return res["data"]
    except Exception as ex:
        raise ex

def delete(collection, id):
    try:
        serverClient = FaunaClient(secret=os.environ.get("FAUNA_SERVER_SECRET"))
        serverClient.query(q.delete(q.ref(q.collection(collection), id)))
        return True
    except Exception as ex:
        raise ex