"""
Re-requesting a Vanity Plate
https://cs50.harvard.edu/python/2022/psets/5/test_plates/
"""

from plates import is_valid

def test_starting_letter():
    assert is_valid("CS50") == True
    assert is_valid("C50S") == False
    assert is_valid("50") == False

def test_length():
    assert is_valid("NRVOUS") == True
    assert is_valid("Nihongo jouzu desune") == False
    assert is_valid("H") == False

def test_num():
    assert is_valid("ECTO88") == True
    assert is_valid("CS50P2") == False
    assert is_valid("CS05") == False

def test_punc():
    assert is_valid("PI3.14") == False
    assert is_valid("CS50!@#$%^&*") == False
"""
The above code is to test the following code called plates.py.


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha():
        if s.isalpha():
            return True
        elif s.isalnum():
            for i in range(len(s)):
                if s[i].isdigit():
                    if s[i:].isdigit() and s[i] != "0":
                        return True
                    else:
                        return False
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
"""
