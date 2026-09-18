# Write a function clean_brand_name(name) that removes leading/trailing 
# spaces and replaces any hyphens '-' with a single space in the input 
# string. Test it with ' oneplus-Nord '

def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name

brand = " oneplus-Nord "
result = clean_brand_name(brand)
print(result)