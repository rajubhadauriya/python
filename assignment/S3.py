# Task-1

followers = 5000
average_rating = 4.5
favorite_app = "Spotify"
is_premium_user = True

"""print("followers : ",followers)
print(type(followers))
print("average rating is : ",average_rating)
print(type(average_rating))
print("favourite app is " ,favorite_app )
print(type(favorite_app))
print("this is premimum user :",is_premium_user)
print(type(is_premium_user))"""

# Task-2

"""order_price=input("enter u r order price : ")
order_price=float(order_price)
gst=order_price*18/100
total_price= order_price+gst
print("order price is : ",order_price)
print("GST is = ",gst)
print("Total bill is : ",total_price)"""

# Task-3

"""product_price_flipkart=["199.99","299.50","150"]
prices=[]

for price in product_price_flipkart:
    prices.append(float(price))
print(prices)
print(sum(prices))"""

# Task-4

def is_discount_applicable(order_amount):
    return order_amount>500
print(is_discount_applicable(450))
print(is_discount_applicable(750))

# Task-5

rating=['4.5','3.0','5','4.2']

new_rating=[]
for r in rating:
    new_rating.append(float(r))
print(max(new_rating))



