# Suppose you have a list of messy product names: [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']. 
# Write code to clean each name (remove spaces, replace hyphens with 
# spaces, and make the brand title case) and print the cleaned list
# .<br><br><em><strong>Constraint:</strong> Use at least three string 
# methods from this session.</em>

products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for product in products:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()

    cleaned_products.append(product)

print(cleaned_products)