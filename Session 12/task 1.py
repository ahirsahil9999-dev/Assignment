# Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. Test it on the prices 100, 250, and 500.

gst_price = lambda price: price + price * 0.18

print(gst_price(100))
print(gst_price(250))
print(gst_price(500))