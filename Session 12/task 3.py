product = ["shop","handwase","clothes","scerum"]

filpcart_product = list(filter(lambda product : product.startswith ("s"), product))

print(filpcart_product)