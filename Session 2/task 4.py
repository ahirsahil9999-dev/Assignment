# Create variables for order_total, delivery_region, and discount_percent
# to represent a Zomato order. Follow Python naming conventions and print 
# a sentence using all three variables, like 'Order from [region] totals 
# ₹[order_total] with [discount_percent]% discount.'

order_total = int(input("Enter Total Orders :"))
delivery_region = input("Enter A Location: ")
dicount_percent = int(input("Enter Discount Percent: "))

print(f"Order from {delivery_region} Totals {order_total} with {dicount_percent}% Dicount.")