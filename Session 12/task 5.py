from functools import reduce

numbers = [40, 60, 80, 120]

doubled = list(map(lambda x: x * 2, numbers))

filtered = list(filter(lambda x: x > 100, doubled))

total = reduce(lambda x, y: x + y, filtered)

print("Doubled:", doubled)
print("Filtered:", filtered)
print("Total:", total)