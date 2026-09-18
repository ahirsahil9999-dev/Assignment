# Write a for loop that goes through a list of Instagram follower
# counts [120, 1500, 23000, 800, 45000] and prints 'Micro', 'Influencer', or 
# 'Celebrity' for each, based on the following: Micro (<1000), 
# Influencer (1000-10000), Celebrity (>10000).<br><br><em><strong>Hint:
# </strong> Use if-elif-else inside the loop to check the follower count range.</em>

followers= [120, 1500, 23000, 800, 45000] 

for counts in followers:
    if counts < 1000:
        print("Mirco")
    elif counts > 1000 and counts < 10000:
        print("Influncer")
    else:
        print("Celebrity")