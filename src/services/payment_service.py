def process_payment(order):
    if order["item"] == "invalid":
        return False

    return True