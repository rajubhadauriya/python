# Task-1
"""import math

number = 25
factorial_number = 5

sqrt_result = math.sqrt(number)

factorial_result = math.factorial(factorial_number)

pi_value = math.pi

print("Square root of", number, ":", sqrt_result)
print("Factorial of", factorial_number, ":", factorial_result)
print("Value of Pi:", pi_value)"""

# Task-2
"""import os

files = os.listdir()

print("Image files found:")

for file in files:
    if file.lower().endswith((".jpg", ".png")):
        print(file)"""

# Task-3
"""from datetime import datetime

try:
    date_input = input("Enter a date (YYYY-MM-DD): ")

    date = datetime.strptime(date_input, "%Y-%m-%d")

    print("Day of the week:", date.strftime("%A"))
except ValueError:
    print("Error: Please enter the date in YYYY-MM-DD format.")"""

# Task-4
def format_follower_count(n):
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n / 1_000:.1f}K"
    else:
        return str(n)

# main.py

from insta_utils import format_follower_count

sample_counts = [950, 1500, 2300000]

for count in sample_counts:
    print(f"{count} -> {format_follower_count(count)}")

# Task-5
# for windows -command prompt
python -m venv venv
venv\Scripts\activate
venv\Scripts\Activate.ps1

import statistics

numbers = [10, 20, 30, 40, 50]

average = statistics.mean(numbers)

print(f"Numbers: {numbers}")
print(f"Average: {average}")



