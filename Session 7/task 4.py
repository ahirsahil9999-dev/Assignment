cart_value = int(input("Enter your Flipkart cart value: "))
payment_method = input("Enter payment method (UPI, Card, Cash): ")

if cart_value > 1000:
    if payment_method == "upi":
        print("Eligible for 10% Cashback")
    else:
        print("Eligible for 5% Cashback")
else:
    print("No cashback")