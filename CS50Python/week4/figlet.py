"""
Frank, Ian and Glen’s Letters
https://cs50.harvard.edu/python/2022/psets/4/figlet/
"""

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 1:
    figlet.setFont(font = random.choice(fonts))
elif len(sys.argv) == 3:
    if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
        figlet.setFont(font = sys.argv[2])
    elif (sys.argv[1] != "-f" or sys.argv[1] != "--font") and sys.argv[2] in fonts:
        sys.exit("The command line argument should start with -f or --font.")
    else:
        sys.exit("Font not found.")
else:
    sys.exit("Should be zero or two command-line arguments.")

input_str = input("Input: ")
print(figlet.renderText(input_str))
