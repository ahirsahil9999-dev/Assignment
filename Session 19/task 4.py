# Create a class called FoodOrder with attributes restaurant_name,
# items (a list), and total_price. Add a method add_item
# (self, item, price) that adds the item to the items list and
# updates total_price. Demonstrate by creating a FoodOrder object
# and adding two items like you would on Zomato.

class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0
        
    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price 
        
order = FoodOrder("Zomato Restaurant")
     
order.add_item("Pizza", 300)
order.add_item("Burger", 100)

print("Restauranr: ", order.restaurant_name)
print("Items: ", order.items)
print("Total Price: ", order.total_price)