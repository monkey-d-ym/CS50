"""
NUMB3RS
https://cs50.harvard.edu/python/2022/psets/7/numb3rs/
"""
import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # number = "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
    # if matches := re.search(r"^" + number + "\." + number + "\." + number + "\." + number + "$",ip):
    matches = re.search(r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip)
    if matches:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
