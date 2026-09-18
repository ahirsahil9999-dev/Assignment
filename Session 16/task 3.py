# Given two lists — one of food items and one of prices — use zip() 
# to print each food item with its price like a Zomato menu 
# (e.g., 'Pizza - ₹250').

food_items = ["pizza","burger","dosa"]
prices = ["400","70","100"]

for food,price in zip(food_items,prices):
    print(f"{food} - {price}")