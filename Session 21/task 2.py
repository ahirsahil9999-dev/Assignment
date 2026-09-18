# Build a class FoodOrder with a method calculate_total() that
# returns the base price. Create a subclass ZomatoOrder that 
# overrides calculate_total() to add a 5% delivery charge.

class FoodOrder:
    def calculate_total(self, base_price):
        return base_price
    

class ZomatoOrder(FoodOrder):
    def calculate_total(self, base_price):
        return base_price + (base_price * 0.05)
    
order = ZomatoOrder()

print("Total Price: ", order.calculate_total(1000))