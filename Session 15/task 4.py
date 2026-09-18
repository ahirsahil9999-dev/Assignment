# Build a Flipkart-style order summary: ask the user for item 
# price and quantity, then calculate and print total price. 
# Use try-except-else-finally blocks to handle ValueError for 
# invalid input, print the total if successful, and always print
# 'Thank you for shopping!' in the finally block.

try:
    price = int(input("Enter A Price: "))
    quantity = int(input("Enter A Quantity: "))

except ValueError:
    print("Please Enter Only Numbers")

else:
    total_price = quantity * price
    print("Total Price:", total_price)

finally:
    print("Thank you for shopping!")