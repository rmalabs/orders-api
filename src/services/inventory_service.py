from db.memory_store import INVENTORY

AUDIT_LOG = []

def reduce_stock(item, quantity):
    if item not in INVENTORY:
        INVENTORY[item] = 5

    INVENTORY[item] -= quantity
    AUDIT_LOG.append({
        "item": item,
        "qty": quantity,
        "remaining": INVENTORY[item]
    })
