# Add getter and setter methods for the _price attribute in your
# Product class to safely access and update the price. Make sure 
# the setter prevents setting a negative price.<br><br><em><strong>
# Hint:</strong> Raise a ValueError if the new price is less than
# zero.</em>

class Product:
    def __init__(self, price):
        self._price = price
        
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        if price < 0:
            raise ValueError("Price Cannot be Negative!")
        self._price = price
        
product = Product(500)

print("Price:", product.get_price())

product.set_price(700)
print("Updated Price:", product.get_price())