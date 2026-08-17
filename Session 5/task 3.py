def last_remove_item(order_list):
    return order_list.pop()

order_list = ["Pizza","Gujarati Thali","Milk","Shampoo"]

result = last_remove_item(order_list)
print("Removed Item:", result)

print("Updated Order:",order_list)
