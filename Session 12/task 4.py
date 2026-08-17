from functools import reduce

orders = [120, 340, 560, 80]

total = reduce(lambda x, y: x + y, orders)

print("Total Bill:", total)