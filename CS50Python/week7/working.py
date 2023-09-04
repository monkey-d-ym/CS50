"""
Working 9 to 5
https://cs50.harvard.edu/python/2022/psets/7/working/
"""
import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    format = re.search(r"^(1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|0?[1-9])(?::([0-5][0-9]))? (AM|PM)$", s)
    if format:
        matches = format.groups()
        start = format_24hr(matches[0], matches[1], matches[2])
        end = format_24hr(matches[3], matches[4], matches[5])
        return f"{start} to {end}"
    else:
        raise ValueError

def valid_min(min):
    return True if 0 <= int(min) <= 59 else False

def format_24hr(hr,min,ampm):
    if ampm == "AM":
        if int(hr) == 12:
            new_hr = 0
        else:
            new_hr = int(hr)
    else:
        if int(hr) == 12:
            new_hr = 12
        else:
            new_hr = int(hr) + 12
    if min == None:
        new_min = ":00"
        return f"{new_hr:02}" + new_min
    else:
        if not valid_min(int(min)) or not valid_min(int(min)):
            raise ValueError
        else:
            new_min = int(min)
            return f"{new_hr:02}" + ":" + f"{new_min:02}"


if __name__ == "__main__":
    main()
