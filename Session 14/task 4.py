# Given a JSON file named user_profile.json containing details 
# like username, followers, and bio (similar to an Instagram 
# profile), use the json module to load the file and print the
# username and number of followers

import json

data = {
    "username" : "Sahil Ahir",
    "followers" : "250",
    "bio" : "Data Analytics"
}

with open("user_profile.json","w") as f:
    json.dump(data, f, indent = 4)
    
print("Json File Created Successfully !")