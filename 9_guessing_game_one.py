import random
from random import randint

randonum = randint(1,10)
#print(randonum)
guess = 0
playing = True

while(playing):
    guess = input("Guess the number between 1 and 10: ")
    guessint=int(guess)

    if (guessint < randonum):
        print("Too low.")
    elif (guessint > randonum):
        print("Too high")
    elif (guessint == randonum):
        print ("You win!")
        playing = False
        








