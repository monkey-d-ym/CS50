"""
Home Federal Savings Bank
https://cs50.harvard.edu/python/2022/psets/1/bank/
"""
greeting = input("Greeting: ").strip().lower()

if greeting.startswith("hello") == 1:
    print("$0")
elif greeting[0] == "h":
    print("$20")
else:
    print("$100")
