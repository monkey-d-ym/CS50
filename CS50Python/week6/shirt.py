"""
CS50 P-Shirt
https://cs50.harvard.edu/python/2022/psets/6/shirt/
"""
import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        ext = [".jpg", ".jpeg",".png"]
        ext_input = os.path.splitext(sys.argv[1])
        ext_output = os.path.splitext(sys.argv[2])
        if ext_input[1].lower() not in ext:
            sys.exit("Invalid input")
        elif ext_output[1].lower() not in ext:
            sys.exit("Invalid output")
        elif ext_input[1].lower() != ext_output[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            try:
                shirt = Image.open("shirt.png")
                muppet = ImageOps.fit(Image.open(sys.argv[1]), shirt.size)
                muppet.paste(shirt, shirt)
                muppet.save(sys.argv[2])
            except FileNotFoundError:
                sys.exit("Input does not exit")

if __name__ == "__main__":
    main()
