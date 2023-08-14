"""
Vanity Plates
https://cs50.harvard.edu/python/2022/psets/2/plates/
"""
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

