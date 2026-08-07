# Task-1

"""def calculate_final_price(price,discount):
        final_price=price-(price*discount)
        return final_price

price=1200
discount=0.15

print(calculate_final_price(price,discount))"""

# Task-2

"""def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 30
    else:
        return 50

print("Delivery Charge:", get_delivery_charge(500))"""

# Task-3

"""def format_cuopon_message(username,discount=10):
    return f"HI {username},you get {discount}% off!"
print(format_cuopon_message("rahul",20))
print(format_cuopon_message("rahul",10))"""

# Task-4

"""def apply_discount(price,rate=0.10):
    return price-(price*rate)
result=apply_discount(1000)
print(result)"""

# Task-5

def calculate_cashback(amount,cashback_rate=0.05):
    return amount*cashback_rate
zomato_cashback=calculate_cashback(500)
flipkart_cashback=calculate_cashback(2000,0.07)
print("zomato cashback is : ",zomato_cashback)
print("flipkart cashback is : ",flipkart_cashback)
