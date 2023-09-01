"""
Lines of Code

"""
import sys
def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if line.lstrip().startswith("#") == 0 and line.isspace() == 0:
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)

if __name__ == "__main__":
    main()
