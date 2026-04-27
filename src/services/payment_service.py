import random

def process_payment(order):
    if order["item"] == "blocked":
        return False

    if order["quantity"] > 5:
        return random.random() > 0.4

    return random.random() > 0.2