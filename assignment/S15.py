# Task-1
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Cannot divide by zero

# Task-2

try:
    reviews = int(input("Enter the number of reviews: "))
    total_stars = int(input("Enter the total stars received: "))

    if reviews > 0:
        average_rating = total_stars / reviews
        print(f"Average Rating: {average_rating:.2f}")
    else:
        print("Number of reviews must be greater than zero.")

except ValueError:
    print("Error: Please enter valid numeric values.")

# Task-3

class InvalidDurationError(Exception):
    pass

def get_playlist_duration(songs):
    total_seconds = 0

    for duration in songs:
        if duration < 0:
            raise InvalidDurationError("Song duration cannot be negative.")
        total_seconds += duration

    return total_seconds / 60  # Convert seconds to minutes

try:
    playlist = [210, 180, 240, 150]
    print("Total Duration:", get_playlist_duration(playlist), "minutes")

    playlist2 = [210, -180, 240]
    print("Total Duration:", get_playlist_duration(playlist2), "minutes")

except InvalidDurationError as e:
    print("Error:", e)

# Task-4
try:
    item_price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    total_price = item_price * quantity

except ValueError:
    print("Error: Please enter valid numeric values.")

else:
    print("Order Summary")
    print("Item Price: ₹", item_price)
    print("Quantity:", quantity)
    print("Total Price: ₹", total_price)

finally:
    print("Thank you for shopping!")

# Task-5

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid numbers.")
