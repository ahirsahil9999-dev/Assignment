prices = [299, 499, 199, 999, 149]
total = 0

for price in prices:
    if price < 200:
        continue
    
    total += price
    
print("Total Price :", total)