# Given a messy text copied from a Zomato review containing
# multiple emails, use re.findall() to extract all valid email
# addresses and print them as a list.

import re

text = """
Great food and fast delivery
For complaints contact: support@zomato.com
Restaurant email: food@gmail.com
My email is sahil123@yahoo.com
Invalid email: hello@com
"""

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = re.findall(pattern, text)

print(emails)