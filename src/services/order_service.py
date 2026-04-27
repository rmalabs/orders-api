from db.memory_store import ORDERS
from services.payment_service import process_payment
from services.inventory_service import reduce_stock

def create_order(data):
    order = {
        "id": len(ORDERS) + 1,
        "item": data.get("item"),
        "quantity": data.get("quantity"),
        "status": "pending"
    }

    reduce_stock(order["item"], order["quantity"])
    success = process_payment(order)

    order["status"] = "completed" if success else "failed"
    ORDERS.append(order)

    return order


def list_orders():
    return ORDERS
