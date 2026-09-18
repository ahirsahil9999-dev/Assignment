# Write a Python program that takes a user's input for the price of a 
# Zomato order as a string, converts it to a float using type casting, 
# adds 18% GST, and prints the final bill amount.

price = input("Enter A Price Of Zomoto Order: ")

price1 = float(price)
print(price1)

gst_amount = price1 * 0.18

final_price = price1 + gst_amount
print("Final Bill Aount :", final_price)