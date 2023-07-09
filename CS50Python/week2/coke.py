"""
Coke Machine
https://cs50.harvard.edu/python/2022/psets/2/coke/
"""
amount_due = 50

while amount_due > 0:
    print("Amount Due:",amount_due)
    insert_coin = int(input("Insert Coin: "))
    while insert_coin == 5 or insert_coin == 10 or insert_coin == 25:
        amount_due -= insert_coin
        if insert_coin != 5 or insert_coin != 10 or insert_coin != 25:
            break

    if amount_due <= 0:
        change_owe = -amount_due
        print("Change Owed:",change_owe)
