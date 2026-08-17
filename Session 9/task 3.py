def format_coupon_message(username, discount=10):
    return f"Hi {username} you get {discount} Off !."

result1 = format_coupon_message("Rahul")
print(result1)

result2 = format_coupon_message("Sahil",20)
print(result2)