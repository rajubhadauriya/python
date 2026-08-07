# Tasks-1

class product:
    def get_discount(self):
        return 0

class electronics(product):
    def get_discount(self):
        return 10

p = product()
e = electronics()

print("Product Discount" , p.get_discount(),"%")
print("Electronic Discount", e.get_discount(),"%")

# Task-2

class foodorder:
    def __init__(self, base_price):
        self.base_price = base_price

    def calculate_total(self):
        return self.base_price

class zomatoorder(foodorder):
    def calculate_total(self):
        delivery_charge = self.base_price * 0.5
        return self.base_price + delivery_charge

order1 = foodorder(500)
order2 = zomatoorder(500)

print("Food Order Total:", order1.calculate_total())
print("Zomato Order Total:", order2.calculate_total())

# Task-3

class influencer:
    def bonus(self):
        return 2000

class brandmanager:
    def bonus(self):
        return 5000

def show_bonus(employee):
    print("Bonus:", employee.bonus())

Influencer = influencer()
manager = brandmanager()

show_bonus(Influencer)  
show_bonus(manager)     

# Task-4

class User:
    def get_status(self):
        return 'active'

class PremiumUser(User):
    def get_status(self):
        return 'premium'

user = User()
pu = PremiumUser()

print("Premium status:", user.get_status())
print("User Premium status:", user.get_status())



