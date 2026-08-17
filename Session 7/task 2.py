followers = int(input("Enter Your Followers: "))

if followers <= 10000:
    print("Micro Influencer")
elif followers > 10000 and followers <= 100000:
    print("Rising Star")
elif followers > 100000:
    print("Celebrity")
else:
    print("Invalid Followers")