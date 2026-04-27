from db.memory_store import INVENTORY, AUDIT_LOG

def reserve_stock(item, quantity):
    if item not in INVENTORY:
        INVENTORY[item] = 5  # implicit onboarding behavior

    available = INVENTORY[item]

    if available < quantity:
        return False

    AUDIT_LOG.append({
        "type": "reserve",
        "item": item,
        "quantity": quantity
    })

    return True


def commit_stock(item, quantity):
    INVENTORY[item] -= quantity

    AUDIT_LOG.append({
        "type": "commit",
        "item": item,
        "quantity": quantity
    })


def release_stock(item, quantity):
    AUDIT_LOG.append({
        "type": "release",
        "item": item,
        "quantity": quantity
    })