products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for product in products:
    product = product.strip()
    product = product.replace("-", " ")
    product = product.title()

    cleaned_products.append(product)

print(cleaned_products)