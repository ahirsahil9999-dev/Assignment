# Given two sets: set1 contains the names of restaurants you have
# ordered from on Zomato, and set2 contains the names of restaurants
# you have ordered from on Swiggy, find and print the union and 
# intersection of these sets.<br><br><em><strong>Hint:</strong> 
# Use the union() and intersection() methods of Python sets.</em>

set1 = {"Dominos", "Pizza Hut", "McDonalds", "Subway"}
set2 = {"Pizza Hut", "Subway", "KFC", "Burger King"}

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))