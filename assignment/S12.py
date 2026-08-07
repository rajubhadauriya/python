# Task-1
"""add_gst = lambda price:price+(price*0.18)
print(add_gst(100))
print(add_gst(250))
print(add_gst(500))"""

# Task-2

"""songs=["shape Of you","blindind lights","Romantic Nights", " lViTing"]
cleaned_songs = list(map(lambda song:song.strip().title(),songs))
print(cleaned_songs)"""

# Task-3
"""products=["Samsung Galaxy","Realme Narzo","sony Headphones","Apple iphone"]
filtered=list(filter(lambda product:product.lower().startswith("s"),products))
print(filtered)"""

# Task-4

"""from functools import reduce
order_Amount = [120,340,560,80]
total_bill = reduce(lambda x,y:x+y,order_Amount)
print("total bill amount",total_bill)"""

# Task-5

from functools import reduce
numbers = [40,60,80,120]

doubled = list(map(lambda x: x*2,numbers))

filtered = list(filter(lambda x: x>100,doubled))
total = reduce(lambda x, y: x+y,filtered)

print("doubled list",doubled)
print("filtered list",filtered)
print("sum",total)
