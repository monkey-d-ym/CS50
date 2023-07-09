"""
camelCase
https://cs50.harvard.edu/python/2022/psets/2/camel/
"""
camelCase = input("variable name in camelCase: ")
print("camelCase:",camelCase)

snake_case = ""
for letter in camelCase:
    if letter.isupper() != 1:
        snake_case += letter
    else:
        lower_case = letter.lower()
        snake_case += "_"
        snake_case += lower_case
print("snake_case:", snake_case)
