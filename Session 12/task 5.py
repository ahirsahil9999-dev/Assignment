# Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process a list of numbers: 
# first double each number, then filter to keep only numbers greater than 100, and finally sum the result. 
# Paste and test the generated code with the list [40, 60, 80, 120].

from functools import reduce

numbers = [40, 60, 80, 120]

doubled = list(map(lambda x: x * 2, numbers))

filtered = list(filter(lambda x: x > 100, doubled))

total = reduce(lambda x, y: x + y, filtered)

print("Doubled:", doubled)
print("Filtered:", filtered)
print("Total:", total)