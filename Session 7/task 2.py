# Create a Python program that takes the number of followers as 
# input and uses if, elif, and else to print 'Micro Influencer' 
# if followers < 10,000, 'Rising Star' if between 10,000 and 
# 100,000, and 'Celebrity' if above 100,000.

followers = int(input("Enter Your Followers: "))

if followers <= 10000:
    print("Micro Influencer")
elif followers > 10000 and followers <= 100000:
    print("Rising Star")
elif followers > 100000:
    print("Celebrity")
else:
    print("Invalid Followers")