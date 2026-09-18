# Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract
# and print only the brand name and the model (i.e., 'Apple' and 'iPhone 14 Pro Max')
# separately.<br><br><em><strong>Hint:</strong> Use split() to help find
# the split point, then use slicing for the substrings.</em>

product = "Apple iPhone 14 Pro Max"

product1 = list(product.split(" "))
print(product1)

brand_name = product1[0]
print(brand_name)

mobile_name = product1[1:]
print(mobile_name)
