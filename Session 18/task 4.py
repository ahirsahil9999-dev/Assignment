# Use re.sub() to mask all but the last 4 digits of any phone
# number in a string (e.g., replace 9876543210 with ******3210) 
# like Paytm does for privacy.<br><br><em><strong>Constraint:
# </strong> Do not use loops; achieve this only with re.sub().</em>

import re

text = "My phone number is 9876543210 and my friend's number is 8123456789."

masked_text = re.sub(r'\d{6}(\d{4})', r'******\1', text)

print(masked_text)