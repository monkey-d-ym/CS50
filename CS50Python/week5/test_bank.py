"""
Back to the Bank
https://cs50.harvard.edu/python/2022/psets/5/test_bank/
"""

from bank import value

def test_hello():
    assert value("Hello, how are you?") == 0
def test_h():
    assert value("How are you?") == 20
def test_noth():
    assert value("What's your name?") == 100

"""
The above code is to test the following code called bank.py

def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")


def value(greeting):
    if greeting.startswith("hello") == 1:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
"""
