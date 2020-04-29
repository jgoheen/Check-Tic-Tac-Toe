import random
from random import randint

randoNum = randint(1000,9999)
randoNum=str(randoNum)

def cows(x, y):
    cowsnbulls = [0, 0]
    for i in range(len(x)):
        if (x[i] == y[i]):
            cowsnbulls[1] += 1
    cowsnbulls[0]=4-cowsnbulls[1]
    return cowsnbulls

guess = ''
playing = True
print("Guess a four digit number.")
print("Every number in the wrong place equals a cow. Every number in the correct place equals a bull.")
print("Game over when you get 4 bulls")

while playing:
        guess=input("Enter a number, exit to quit: ")
        if guess == 'exit':
            break
        numofcows = cows(guess, randoNum)
        print("number of cows: ", numofcows[0])
        print("number of bulls: ", numofcows[1])
        if numofcows[1] == 4:
            print("you win!")
            playing = False





