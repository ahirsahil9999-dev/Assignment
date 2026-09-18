# Write a Python function using re.search() that checks if a 
# given string contains a valid date in the format DD/MM/YYYY 
# (e.g., 25/06/2024), and returns True if found, otherwise False.
# <br><br><em><strong>Hint:</strong> Use the pattern
# '\b\d{2}/\d{2}/\d{4}\b'.</em>

import re

def check_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    if re.search(pattern, text):
        return True
    else:
        return False


print(check_date("My birthday is 12/01/2004"))
print(check_date("Today is a good day"))