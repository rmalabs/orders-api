from services.order_service import create_order, list_orders

def handle_orders(method, request, data=None):
    if method == "GET":
        return list_orders()

    if method == "POST":
        return create_order(data)