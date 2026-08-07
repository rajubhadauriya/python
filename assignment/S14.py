# Task-1
# Create and write to the file
with open("my_playlist.txt", "w") as file:
    file.write("Tere Bin\n")
    file.write("Chand Mera Dil\n")
    file.write("Dil Diwana\n")
    file.write("SAAJAN MERA\n")
    file.write("Koi Mil Gaya\n")

print("Playlist saved to my_playlist.txt")

# Task-2

with open("my_playlist.txt", "r") as file:
    for song in file:
        print(song.strip().upper())

# Task-3

"""with open("ipl_matches.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    print("Winning Teams:")
    for row in reader:
        print(f"Match {row['Match']}: {row['Winner']}")"""

# Task-4 
"""import json

# Open and load the JSON file
with open("user_profile.json", "r") as file:
    profile = json.load(file)

# Print the username and followers
print("Username:", profile["username"])
print("Followers:", profile["followers"])"""

# Task-5
from pathlib import Path

# Create a Path object for the file
file_path = Path("zomato_orders.json")

# Check if the file exists
if file_path.exists():
    print("zomato_orders.json was found in the current directory.")
else:
    print("zomato_orders.json was not found in the current directory.")
