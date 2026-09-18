# Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' (case-insensitive).

product = ["shop","handwase","clothes","scerum"]

filpcart_product = list(filter(lambda product : product.startswith ("s"), product))

print(filpcart_product)