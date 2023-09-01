"""
Scourgify
https://cs50.harvard.edu/python/2022/psets/6/scourgify/
"""

import sys
import csv

def main():

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    students_before = []
    students_after = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_before.append(row)
        for student in students_before:
            last, first = student["name"].split(", ")
            house = student["house"]
            students_after.append({"first": first, "last": last, "house": house})
        fieldnames = ["first", "last", "house"]
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in students_after:
                writer.writerow(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()
