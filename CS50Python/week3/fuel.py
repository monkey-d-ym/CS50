"""
Fuel Gauge
https://cs50.harvard.edu/python/2022/psets/3/fuel/
"""
while True:
    fuel = input("Fraction: ")
    try:
        num, deno = fuel.split("/")
        fraction = int(num)/int(deno)
        if fraction <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
percentage = round(fraction * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(str(percentage) + "%")
