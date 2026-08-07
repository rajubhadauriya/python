# Task-1

"""def reverse_string(s):
    if s=="":
        return ""
    return reverse_string(s[1:])+s[0]
text = "hello"
print(reverse_string(text))"""

# Task-2

"""def sum_playlist_duration(durations):
    if len(durations)==0:
        return 0
    return durations[0]+sum_playlist_duration[1:]

playlist = [180,240,200,300]
total_duration = sum_playlist_duration(playlist)

print("total playlist duration : ",total_duration,"seconds")"""

# Task-3

"""count = 10
def update_count():
    count = 5
    print("inside : ",count)
update_count()
print("outside",count)"""

# Task-4

"""def count_likes(posts):
    total = posts["likes"]
    for reply in posts.get("replies",[]):
        total+=count_likes(reply)
    return total

posts = {
    "likes": 10,
    "replies": [
        {
            "likes": 5,
            "replies": [
                {
                    "likes": 2,
                    "replies": []
                }
            ]
        },
        {
            "likes": 3,
            "replies": []
        }
    ]
}    
print(count_likes(posts))"""

# Task-5
# global variable
"""app_status = "WhatsApp is Running"

def check_user_status():
    # Local variable
    user_status = "Online"

    print("Inside function:")
    print("User Status (local):", user_status)
    print("App Status (global):", app_status)
    print()

# Before function call
print("Before function call:")
print("App Status (global):", app_status)
print()

# Function call
check_user_status()

# After function call
print("After function call:")
print("App Status (global):", app_status)

# Trying to access the local variable outside the function
try:
    print("User Status (local):", user_status)
except NameError:
    print("User Status (local): Not accessible outside the function.")"""