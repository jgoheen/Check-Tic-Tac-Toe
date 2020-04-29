import random
from random import randint

randonum = randint(1,10)
#print(randonum)
guess = 5
playing = True

number = input("Enter a number between 1 and 10 and I will guess it: ")

while(playing):
    if guess == number:
        playing = False
        break
    print('Computers guess is: ', guess)
    status = input("High, Low, or Correct? ")
    if status == "High":
        guess = guess - 1
    elif status == "Low":
        guess = guess + 1
    elif status == "Correct":
        print("computer wins!")
        playing = False
            








