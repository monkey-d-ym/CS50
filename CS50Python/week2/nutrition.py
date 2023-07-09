"""
Nutrition Facts
https://cs50.harvard.edu/python/2022/psets/2/nutrition/
"""
fruit_nutrition = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe" : 50,
    "grapefruit" : 60,
    "grape" : 90,
    "honeydew melon" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 15,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tagerine" : 50,
    "watermelon" : 80
}

fruit = input("Item: ").lower()

if fruit in fruit_nutrition:
    print("Calories: ",fruit_nutrition[fruit])

