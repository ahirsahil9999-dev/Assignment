# Build a Python script that asks the user for their Zomato order
# total and prints 'Apply Free Delivery' if total is above 299, 
# 'Add more items for free delivery' if between 200 and 299, 
# else 'Delivery charges apply'.

order_total = int(input("Enter your Zomato order total: "))

if order_total > 299:
    print("Apply Free Delivery")

elif order_total >= 200 and order_total <= 299:
    print("Add more items for free delivery")

else:
    print("Delivery charges apply")