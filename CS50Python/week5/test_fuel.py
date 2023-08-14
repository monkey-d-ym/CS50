"""
Refueling
https://cs50.harvard.edu/python/2022/psets/5/test_fuel/
"""

from fuel import convert, gauge
import pytest

def test_convert():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    assert convert("3/4") == 75
    assert convert("0/100") == 0
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(0.01) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(75) == "75%"

"""
The above code is to test the following code called fuel.py


def main():
    while True:
        fraction = input("Fraction: ")
        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    num, deno = fraction.split("/")
    ratio = int(num)/int(deno)
    if ratio <= 1:
        return round(ratio * 100)
    elif int(deno) == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
"""
