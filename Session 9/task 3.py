# Build a function called format_coupon_message(username, discount=10)
# that returns a string like 'Hi Rahul, you get 10% off!' If no 
# discount is given, use 10% by default. Test it for two users: 
# one with a custom discount, one with the default.

def format_coupon_message(username, discount=10):
    return f"Hi {username} you get {discount} Off !."

result1 = format_coupon_message("Rahul")
print(result1)

result2 = format_coupon_message("Sahil",20)
print(result2)