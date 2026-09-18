# Build a simple custom module named insta_utils.py with a function
# format_follower_count(n) that returns '1.5K' for 1500 and '2.3M' for
# 2300000. Import and use this function in another script to display 
# formatted counts for 3 sample numbers.

def format_follower_count(n):
    if n >= 1000000:
        return str(round(n / 1000000, 1)) + "M"
    elif n >= 1000:
        return str(round(n / 1000, 1)) + "K"
    else:
        return str(n)