"""
Grocery List
https://cs50.harvard.edu/python/2022/psets/3/grocery/
"""

grocery_list = []
grocery_dict = {}

try:
    while True:
        item = input("").upper()
        grocery_list.append(item)
        grocery_list.sort()
except EOFError:
    for grocery in grocery_list:
        if grocery in grocery_dict:
            grocery_dict[grocery] += 1
        else:
            grocery_dict[grocery] = 1
    for grocery in grocery_dict:
        print(grocery_dict[grocery],grocery)
