import json
from services.order_service import create_order, list_orders


def handle_request(path, method, body):
    if path == "/orders" and method == "POST":
        data = json.loads(body)
        return create_order(data)

    if path == "/orders" and method == "GET":
        return list_orders()

    return {"error": "Not found"}