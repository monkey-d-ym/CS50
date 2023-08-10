"""
Testing my twttr
https://cs50.harvard.edu/python/2022/psets/5/test_twttr/
"""
from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("TWITTER") == "TWTTR"

def test_letter():
    assert shorten("TwittEr20") == "Twttr20"

def test_punctuation():
    assert shorten("twitter;cs50.") == "twttr;cs50."

"""
The above test is to test the following code called twttr.py

def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    lower_vowels = ["a", "e", "i", "o", "u"]
    upper_vowels = []
    for vowel in lower_vowels:
        upper_case = vowel.upper()
        upper_vowels.append(upper_case)
    all_vowels = lower_vowels + upper_vowels
    no_vowel = ""
    for letter in word:
        if letter not in all_vowels:
            no_vowel += letter
    return no_vowel

if __name__ == "__main__":
    main()
"""
