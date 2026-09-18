# Given a function apply_discount(price, rate=0.10), update it so 
# that if the rate is not passed, it uses 0.10 by default. Then, 
# call it with only the price argument and print the result.<br>
# <br><em><strong>Hint:</strong> Use default arguments in your 
# function definition.</em>

def apply_discount(price, rate=0.10):
    discount = price * rate
    final_price = price - discount
    return final_price

result = apply_discount(1000)

print(result)