"""
Adieu, Adieu
https://cs50.harvard.edu/python/2022/psets/4/adieu/
"""

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Names: ")
        names.append(name)
    except EOFError:
        break

lyrics = p.join(names)
print("Adieu, adieu, to " + lyrics)
