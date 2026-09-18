import re

pattern = r'^OD\d{18}$'

order1 = "OD123456789012345000"
order2 = "AB123456789012345000"
order3 = "OD12345"

if re.search(pattern, order1):
    print("Valid Order ID")
else:
    print("Invalid Order ID")

if re.search(pattern, order2):
    print("Valid Order ID")
else:
    print("Invalid Order ID")

if re.search(pattern, order3):
    print("Valid Order ID")
else:
    print("Invalid Order ID")