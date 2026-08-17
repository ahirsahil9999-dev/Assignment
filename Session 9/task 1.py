def calculate_final_price(price,discount_rate):
    discount_rate = price * 0.15
    final_price = price - discount_rate
    return final_price
    
result = calculate_final_price(1200,0.15)
print(result)