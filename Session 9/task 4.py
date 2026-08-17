def apply_discount(price, rate=0.10):
    discount = price * rate
    final_price = price - discount
    return final_price

result = apply_discount(1000)

print(result)