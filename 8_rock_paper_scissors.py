p1 = input('p1, type your move. "paper", "rock", "scissors" or "enter" to quit: ')
p2 = input('p2, type your move. "paper", "rock", "scissors" or "enter" to quit: ')

while (p1 != "enter") and (p2 != "enter"):
    if (p1 == "rock") and (p2 == "scissors"):
        print("p1 wins!")
    elif (p1 == "scissors") and (p2 == "paper"):
        print("p1 wins!")
    elif (p1 =="paper") and (p2 == "rock"):
        print("p1 wins!")
    elif(p1 == p2):
        print("tie!")
    else:
        print("p2 wins")
    p1 = input('p1, type your move. "paper", "rock", "scissors" or "enter" to quit: ')
    p2 = input('p2, type your move. "paper", "rock", "scissors" or "enter" to quit: ')






