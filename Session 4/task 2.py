def clean_brand_name(name):
    name = name.strip()
    name = name.replace("-", " ")
    return name


brand = " oneplus-Nord "

result = clean_brand_name(brand)

print(result)