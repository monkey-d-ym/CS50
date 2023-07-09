"""
Meal Time
https://cs50.harvard.edu/python/2022/psets/1/meal/
"""
def main():
    meal_time = input("What's the time now?: ")
    t = convert(meal_time)
    if 8.00 >= t >= 7.00:
        print("breakfast time")
    if 13.00 >= t >= 12.00:
        print("lunch time")
    if 19.00 >= t >= 18.00:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    min_float = round(int(minutes)/60,2)
    return int(hours) + min_float


if __name__ == "__main__":
    main()
