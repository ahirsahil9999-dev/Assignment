# Build a function is_discount_applicable(order_amount) that takes a 
# float and returns True if the amount is greater than 500, otherwise 
# False. Print the result for order amounts 450 and 750.

def is_discount_applicable(order_amount):
    if order_amount > 500:
        return True
    else:
        return False
    
print(is_discount_applicable(450))
print(is_discount_applicable(750))
