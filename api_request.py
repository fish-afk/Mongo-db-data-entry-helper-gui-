import requests
import json
from dotenv import load_dotenv
import os

URL = "https://data.mongodb-api.com/app/data-zwuiq/endpoint/data/beta/action/insertOne"

load_dotenv(".env")
SECRET_KEY = os.environ.get("API_KEY")


def destructure(value):
    if value.lower() == "true":
        return True
    else:
        return False

def post_record(args, collection, length):
    payload = json.dumps({
        "collection": collection,
        "database": "Kits",
        "dataSource": "Cluster1",
        "document": {
            "teamname": args[0],
            "name": args[1],
            "price": args[2],
            "description": args[3],
            "img_src": args[4],
            "is_customizable": destructure(args[5]),
            "qty": args[6],
            "id": length

        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': SECRET_KEY
    }

    response = requests.request("POST", URL, headers=headers, data=payload)
    print(response.text)
    return response.status_code
