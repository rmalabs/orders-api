from db.memory_store import ORDERS
from services.inventory_service import (
    reserve_stock,
    commit_stock,
    release_stock
)
from services.payment_service import process_payment


def create_order(data):
    order = {
        "id": len(ORDERS) + 1,
        "item": data.get("item"),
        "quantity": data.get("quantity"),
        "status": "pending"
    }

    reserved = reserve_stock(order["item"], order["quantity"])

    if not reserved:
        order["status"] = "rejected"
        ORDERS.append(order)
        return order

    payment_success = process_payment(order)

    if payment_success:
        commit_stock(order["item"], order["quantity"])
        order["status"] = "completed"
    else:
        release_stock(order["item"], order["quantity"])
        order["status"] = "failed"

    ORDERS.append(order)
    return order


def list_orders():
    return ORDERS