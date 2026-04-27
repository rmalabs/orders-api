import random

def process_payment(order):
    if order["item"] == "blocked":
        return False

    return random.choice([True, True, True, False])
