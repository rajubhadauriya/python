# Task-1

"""playlist_ids=[101,205,309,412,518]
playlist_ids.append(625)
print(playlist_ids)"""

# Task-2

"""cart_items = ['t-shirt','shoes']
cart_items1 = ['jeans','cap']
cart_items.extend(cart_items1)
print(cart_items)"""

# Task-3

"""def remove_last_item(order_list):
    removed_item = order_list.pop()
    return removed_item
order_list=["Pizza","Burger","Coke","Fries"]
removed=remove_last_item(order_list)
print("remove items :",removed)
print(order_list)"""

# Task-4

insta_filter = ("Clarendon","Juno","Lark","Gingham")
insta_filter[1]="Valencia"
#Explanation:
#TypeError:'tuple' object does not support item assignment
#because tuples are immutable

# Task-5
favorite_genres= ["Action","Comedy","Romance"]
#Explanation: A list is used because the user's favorite genres can be added,removed,or changed.

train_class = ("Sleeper","General","AC 3 Tier","AC 2 Tier")
#Explanation: A tuple is used because the train classes are fixed and should not modified.