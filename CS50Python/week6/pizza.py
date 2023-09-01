"""
Pizza Py
https://cs50.harvard.edu/python/2022/psets/6/pizza/
"""
import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    pizza = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                pizza.append(row)
            print(tabulate(pizza, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()
