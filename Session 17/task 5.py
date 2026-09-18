# Create a new virtual environment using venv, activate it, and install 
# the statistics and requests packages via pip. Then, write a script that
# uses statistics.mean() to calculate the average of a list of numbers.

import statistics

numbers = [10, 20, 30, 40, 50]

average = statistics.mean(numbers)

print("Average:", average)