"""
Guessing Game
https://cs50.harvard.edu/python/2022/psets/4/game/#guessing-game
"""

import random
while True:
    n = input("Level: ")
    if n.isnumeric() == 1 and int(n) > 0:
        break


rand_num = random.randint(1,int(n))

while True:
    guess = input("Guess: ")
    if guess.isnumeric() == 1 and 0 < int(guess) <= int(n):
        if int(guess) < rand_num:
            print("Too small!")
        elif int(guess) > rand_num:
            print("Too large!")
        else:
            print("Just right!")
            break
