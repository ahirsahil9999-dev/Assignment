# read a json file
import json

with open("user_profile.json","r") as f:
    data = json.load(f)
    
print("Username:", data["username"])
print("Followers:", data["followers"])