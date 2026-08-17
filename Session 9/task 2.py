def get_delivery_charge(amount, city):
    if city == "Ahmedabad":
        return 30
    else:
        return 50

charge1 = get_delivery_charge(500, "city")
print("Ahmedabad delivery charge:", charge1)

charge2 = get_delivery_charge(500, 'Mumbai')
print("Mumbai delivery charge:", charge2)