"""
Response Validation
https://cs50.harvard.edu/python/2022/psets/7/response/
"""
from validator_collection import checkers

def main():

    address = input("What's your email address?: ").strip()

    if checkers.is_email(address):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
