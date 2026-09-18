# Create a Python program that accepts a date in 'YYYY-MM-DD' format 
# from the user and displays the day of the week using the datetime 
# module.

from datetime import datetime

date = input("Enter Your Birthdate like 'YYYY-MM-DD': ")

date_object = datetime.strptime(date, "%Y-%m-%d")

day = date_object.strftime("%A")

print("Day:", day)