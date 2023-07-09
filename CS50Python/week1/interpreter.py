"""
Math Interpreter
https://cs50.harvard.edu/python/2022/psets/1/interpreter/
"""
expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
else:
    if int(z) != 0:
        print(float(x) / float(z))
    else:
        print("undefined")
