# Given a list of strings representing product prices from Flipkart, like
# ['199.99', '299.50', '150'], convert all to floats and calculate the 
# total cart value.

prices = ['199.99','299.50','150']

new_prices = []

for price in prices:
    new_prices.append(float(price))
    
print(new_prices)

total_price = sum(new_prices)

print(total_price)