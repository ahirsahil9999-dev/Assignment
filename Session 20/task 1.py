# Create a Python class called Product with a private attribute _price.
# Initialize _price in the constructor and write a method to 
# display its value.

class Product:
    def __init__(self, price):
        self.price = price
        
    def display_price(self):
        print("Price: ", self.price)
        
product = Product(500)

product.display_price()