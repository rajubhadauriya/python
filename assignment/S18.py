# Task-1

import re

text = """
Call me at 9876543210.
My old number was 8123456789.
Price is 25000.
Order ID: 123456.
Another contact: 7654321098.
Invalid numbers: 6123456789, 1234567890."""


pattern = r'[789]\d{9}'

phone_num = re.findall(pattern , text)

print("Valid Indian Phone numbers: ")
for number in phone_num:
    print(number)


# Task-2
import re

def check_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'

    if re.search(pattern, text):
        return True
    else:
        return False

print(check_date("Meeting date is 25/06/2024"))   
print(check_date("Meeting date is 2024-06-25"))  


# Task-3
import re

text = """
Great food! Contact us at support@zomato.com
For offers email sales@gmail.com
Or write to helpdesk@yahoo.in
"""

pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

emails = re.findall(pattern, text)

print(emails)


# Task-4

import re

text = "My number is 9974989445"

result = re.sub(r'(\d{6})(\d{4})', r'******\2', text)

print(result)


# Task-5

import re

order = "Your order ID is OD123456789012345000"

pattern = r"OD\d{18}"

match = re.search(pattern, order)

if match:
    print("Valid Order ID:", match.group())
else:
    print("Invalid Order ID")

