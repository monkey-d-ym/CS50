"""
Outdated
https://cs50.harvard.edu/python/2022/psets/3/outdated/
"""
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ").strip()
    if "/" in date:
        month, day , year = date.split("/")
    elif "," in date:
        month_day, year = date.split(",")
        month, day = month_day.split(" ")
        if month in months:
            month = months.index(month) + 1
    else:
        continue

    try:
        if int(day) > 31 or int(month) > 12:
            continue
        else:
            break
    except ValueError:
        continue
print(f"{year}-{int(month):02}-{int(day):02}")
