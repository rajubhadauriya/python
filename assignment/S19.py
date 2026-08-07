# Tasks-1 

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

song1 = Song("Kesariya", "Arijit Singh", 270)

print("Title:", song1.title)
print("Artist:", song1.artist)
print("Duration:", song1.duration, "seconds")

# Task-2

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = title
        self.duration = duration

song1 = Song("Kesariya", "Arijit Singh", 270)

print("Title:", song1.title)
print("Artist:", song1.artist)


# Task-3

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")


song1 = Song("Kesariya", "Arijit Singh", 270)

song1.play_preview()


# Task-4

class FoodOrder:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.items = []
        self.total_price = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total_price += price


order = FoodOrder("Domino's")

order.add_item("Pizza", 250)
order.add_item("Burger", 120)

print("Restaurant:", order.restaurant_name)
print("Items:", order.items)
print("Total Price:", order.total_price)

# Task-5

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.play_count = 0

    def increment_play_count(self):
        self.play_count += 1


song1 = Song("Kesariya", "Arijit Singh", 270)

song1.increment_play_count()
song1.increment_play_count()
song1.increment_play_count()

print("Title:", song1.title)
print("Play Count:", song1.play_count)