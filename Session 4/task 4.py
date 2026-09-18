# Build a function format_product_display(name, price) that takes a 
# product name and price (e.g., 'Boat Earbuds', 1299) and returns a 
# formatted string like 'Boat Earbuds - ₹1299'.

def format_product_display(name, price):
    
    return f"{name} - {price}"
    
result = format_product_display("Boat Earbuds",1299)
print(result)