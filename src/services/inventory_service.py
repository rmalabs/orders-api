from db.memory_store import INVENTORY

def reduce_stock(item, quantity):
    if item not in INVENTORY:
        INVENTORY[item] = 10

    INVENTORY[item] -= quantity