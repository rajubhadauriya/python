# Tasks-1 

class product:
    def __init__(self,price):
        self.__price = price

    def display_price(self):
        print("Price:", self.__price)

p = product(25000)
p.display_price()

# Task-2

class Product:
    def __init__(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = new_price

p= Product(2999)

print("Price:", p.get_price())   # Price: 2999

p.set_price(3999)
print("Updated Price:", p.get_price())  #  Updated Price: 3999

# Task-3

class Playlist:
    def __init__(self):
        self.__songs = []

    def add_song(self, song):
        self.__songs.append(song)

    def remove_song(self, song):
        self.__songs.remove(song)

    def get_songs(self):
        return self.__songs

p = Playlist()

p.add_song("Song 1")
p.add_song("Song 2")

print(p.get_songs()) # ['Song 1', 'Song 2']

p.remove_song("Song 1")

print(p.get_songs())  # ['Song 2']

# Task-4

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using UPI")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

u = UPI()
c = CreditCard()

u.pay(500)
c.pay(1000)

