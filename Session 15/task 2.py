# Simulate a Zomato-style rating system: ask the user for number
# of reviews and total stars, then calculate average rating. Use
# try-except to handle invalid (non-numeric) input and print an 
# error message if input is not a number.<br><br><em><strong>Hint:</strong> 
# Use input() and int() conversion inside a try block.</em>

try:
    reviews = int(input("Enter number of reviews: "))
    stars = int(input("Enter total stars: "))
    
    average_rating = stars / reviews
    print("Average Rating:", average_rating)
    
except ValueError:
    print("Please Enter Only Number")