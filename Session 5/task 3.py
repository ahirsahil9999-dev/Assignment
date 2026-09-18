# Write a function remove_last_item(order_list) that pops the last item 
# from a Zomato order list and returns the removed item. Test it with a 
# sample order_list.

def last_remove_item(order_list):
    return order_list.pop()

order_list = ["Pizza","Gujarati Thali","Milk","Shampoo"]

result = last_remove_item(order_list)
print("Removed Item:", result)

print("Updated Order:",order_list)
