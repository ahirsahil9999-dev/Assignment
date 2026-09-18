# Write a Python script that checks if a user's entered age is 18 
# or above and prints 'Eligible for IPL ticket booking' if true, 
# otherwise prints 'Not eligible'.

age = int(input("Enter Your Age: "))

if age >= 18:
    print("Eligible for IPL ticket booking")
else:
    print("Not Eligible for IPL ticket booking")