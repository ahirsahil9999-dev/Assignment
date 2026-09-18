# Use pathlib to check if a file called zomato_orders.json exists
# in your current directory, and print an appropriate message if 
# it is found or not.<br><br><em><strong>Hint:</strong> Use Path
# ('zomato_orders.json').exists() from the pathlib module.</em>

import os

if os.path.exists("zomato_orders.json"):
    print("Folder Already Exists")
else:
    os.mkdir("zomato_orders.json")
    print("Created !!")
    