
"""
Little Professor
https://cs50.harvard.edu/python/2022/psets/4/professor/

"""

import random


def main():
    level = get_level()
    round = 0
    score = 0
    while round < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        trial = 0
        # ans = input(f"{x} + {y} = ")
        while True:
            ans = input(f"{x} + {y} = ")
            if ans == str(x + y):
                score += 1
                break
            else:
                if trial < 2:
                    print("EEE")
                    trial += 1
                else:
                    print(f"{x} + {y} = {x + y}")
                    break
        round += 1
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level.isnumeric() == 1 and int(level) in [1,2,3]:
            level = int(level)
            return level
        #else:
            #raise ValueError("Invalid level input. Please enter a numeric value between 1 and 3.")


def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
