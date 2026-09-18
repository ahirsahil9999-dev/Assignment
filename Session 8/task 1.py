# Create a Python list called order_amounts with the values 
# [120, 250, 90, 310, 150]. Use a for loop to calculate and 
# print the total order value.

Order_list = [120, 250, 90, 310, 150]
total_amount = 0

for amount in range(len(Order_list)):
    total_amount += Order_list[amount]
    
print("Total Amount :", total_amount)