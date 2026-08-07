# Task-1
movies = [
    "Dabangg",
    "3 Idiots",
    "12th Fail",
    "SPIDERMAN",
    "RAMAYAN"
]

movie_iterator = iter(movies)

try:
    while True:
        print(next(movie_iterator))
except StopIteration:
    print("All movies displayed.")

# Task-2

playlist = [
    "TERE MAST MAST NAIN",
    "JANEMAN",
    "Tum Hi Ho",
    "ruka ja",
    "Tera Bin ",
    "mera pyar"
]

for position, song in enumerate(playlist, start=1):
    print(f"{position}. {song}")

# Task-3

food_items = ["Pizza","Burger","Pasta","Biryani","Sandwich"]

prices = [250,150,200,300,120]

for food, price in zip(food_items, prices):
    print(f"{food} - ₹{price}")

# task-4

def insta_posts_generator(posts):
    for post in posts:
        yield post

posts = [
    "Sunset vibes ",
    "Coffee and calm mornings ",
    "Exploring new places ",
    "Fitness journey ",
    "Weekend memories "
]

post_generator = insta_posts_generator(posts)

try:
    while True:
        print(next(post_generator))
except StopIteration:
    print("All posts have been displayed.")

# Task-5
def cashback_generator(transactions):
    for amount in transactions:
        cashback = amount * 0.05
        yield cashback

transactions = [500, 1200, 750, 2000, 350]

cashback = cashback_generator(transactions)

for value in cashback:
    print(f"Cashback received: ₹{value:.2f}")
