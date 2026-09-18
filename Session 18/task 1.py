# Use re.findall() to extract all valid Indian phone numbers
# (10 digits, starting with 7, 8, or 9) from a given text string 
# that contains random numbers, prices, and phone numbers like
# those seen in OLX or WhatsApp chats.

import re

text = """
OLX price is 25000.
Contact me on 9876543210.
Another number is 8123456789.
Random number 1234567890.
WhatsApp: 7654321098.
"""

pattern = r'\b[789]\d{9}\b'

phone_numbers = re.findall(pattern, text)

print("Valid Indian phone numbers:")
for number in phone_numbers:
    print(number)
