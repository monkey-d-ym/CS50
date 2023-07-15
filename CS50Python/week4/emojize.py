"""
emojize
https://cs50.harvard.edu/python/2022/psets/4/emojize/

install -> pip install emoji
"""

import emoji

input_str = input("Input: ")
output_str = emoji.emojize(input_str, language = "alias")
print("Output: ", output_str)
