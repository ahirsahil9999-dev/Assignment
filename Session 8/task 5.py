followers= [120, 1500, 23000, 800, 45000] 

for counts in followers:
    if counts < 1000:
        print("Mirco")
    elif counts > 1000 and counts < 10000:
        print("Influncer")
    else:
        print("Celebrity")