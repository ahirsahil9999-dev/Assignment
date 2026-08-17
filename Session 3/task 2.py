price = input("Enter A Price Of Zomoto Order: ")

price1 = float(price)
print(price1)

gst_amount = price1 * 0.18

final_price = price1 + gst_amount
print("Final Bill Aount :", final_price)