"""
Just setting up my twttr
https://cs50.harvard.edu/python/2022/psets/2/twttr/
"""
lower_vowels = ["a", "e", "i", "o", "u"]
upper_vowels = []
for vowel in lower_vowels:
    upper_case = vowel.upper()
    upper_vowels.append(upper_case)
all_vowels = lower_vowels + upper_vowels

input_text = input("Input: ")
for letter in input_text:
    if letter in all_vowels:
        print("", end = "")
    else:
        print(letter, end = "")
print("")
