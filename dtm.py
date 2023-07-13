import re


def order_check(order_no):  # rather checking order number
    if 11 <= len(order_no) <= 14:
        if re.match('^[A-Za-z0-9_]+$', order_no):
            return True
        else:
            return False
    else:
        return False
