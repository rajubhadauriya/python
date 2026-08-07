# Task-1

"""user_age = int(input("enter your age : "))
if user_age >=18:
    print("Eligible for IPL ticket booking")
else:
    print("Not Eligible")"""

# Task-2

"""follwers=int(input( "enter number of follwers : "))
if follwers<10000:
    print("micro influencer")
elif follwers<=100000:
    print("Rising star")
else:
    print("Celebrity")"""

# Task-3

"""total=float(input("enter your order total : "))
if total>299:
    print("Apply Free Delivery")
elif total >=200:
    print(" Add more order for free delivery")
else:
    print("delivery charges apply")"""

# Task-4
cart_value = float(input("enter flipkart cart value"))
payment_method =input("enter payment method (UPI/CARD/Cash):")

if cart_value>1000:
    if payment_method=="UPI":
        print("eligible for 10% cashback")
    else:
        print("eligible for 5% cashback")
else:
    print("no cashback")