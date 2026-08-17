def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False
    
print(is_discount_applicable(450))
print(is_discount_applicable(750))
