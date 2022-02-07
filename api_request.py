import requests
import json
from main import SECRET_KEY

url = "https://data.mongodb-api.com/app/data-zwuiq/endpoint/data/beta/action/insertOne"


def destructure(value):
    if value.lower() == "true":
        return True
    else:
        return False


def post_record(*args, **kwargs):
    payload = json.dumps({
        "collection": "other_kits",
        "database": "Kits",
        "dataSource": "Cluster1",
        "document": {
            "teamname": args[0][0],
            "name": args[0][1],
            "price": float(args[0][2]),
            "description": args[0][3],
            "img_src": args[0][4],
            "is_customizable": destructure(args[0][5]),
            "qty": int(args[0][6])

        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': SECRET_KEY
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.status_code
