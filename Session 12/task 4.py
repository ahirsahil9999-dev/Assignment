# Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the total bill amount.

from functools import reduce

orders = [120, 340, 560, 80]

total = reduce(lambda x, y: x + y, orders)

print("Total Bill:", total)