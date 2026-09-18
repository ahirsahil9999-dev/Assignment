# Write a function show_bonus(employee) that takes any object with 
# a bonus() method and prints the result. Test it with two classes:
# Influencer (bonus returns 2000) and BrandManager (bonus returns 5000),
# demonstrating polymorphism.

class Influencer:
    def bonus(self):
        return 2000
    
class BrandManager:
    def bonus(self):
        return 5000
    
def show_bonus(employee):
    print("Bonus: ", employee.bonus())
    
influencer = Influencer()
manager = BrandManager()

show_bonus(influencer)
show_bonus(manager)