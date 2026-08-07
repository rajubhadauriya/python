#Task-1

mobile= "Redmi Note 12"
print("Lowercase : ",mobile.lower())
print("Uppercase : ",mobile.upper())

# Task-2
def clean_brand_name(name):
    return name.strip().replace("-"," ")
brand= " oneplus-Nord "
print(clean_brand_name(brand))

# Task-3

text = "Apple iPhone 14 Pro Max"
split_text=text.split()
print(split_text)
print(text.split()[0])
print(text.split()[1])

# Task-4
def format_display(name,price):
    return f"{name}-\u20b9{price}"
print(format_display("Boat Earbuds",1299))

# Task-5
products=['mi-Band 5','SAMSUNG-Galaxy','Realme-Book']
clean_data=[products[0].strip().replace("-"," ").title(),products[1].strip().replace("-"," ").title(),
            products[2].strip().replace("-"," ").title()]
print(clean_data)