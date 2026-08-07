# Task-1
order_amounts = [120,250,90,310,150]
total = 0

"""for i in order_amounts:
    total+=i
print(total)"""

# Task-2
"""cricket_score = [45,78,102,34,67,89]
i = 0
while i< len(cricket_score):
    if cricket_score[i]>100:
        break
    print(cricket_score[i])
    i+=1"""
    
# Task-3

prices = [299, 499, 199, 999, 149]
total = 0

"""for price in prices:
    if price < 200:
        continue  # Skip items priced below 200
    total += price

print("Total of items priced 200 or above:", total)"""

# Task-4

# List of favorite songs
"""songs = ['Kesariya', 'Believer', 'Shape of You', 'Blinding Lights', 'Excuses']


for position, song in enumerate(songs, start=1):
    print(f"{position}. {song}")"""

# Task-5
followers = [120, 1500, 23000, 800, 45000]

for count in followers:
    if count < 1000:
        print(f"{count}: Micro")
    elif count <= 10000:
        print(f"{count}: Influencer")
    else:
        print(f"{count}: Celebrity")