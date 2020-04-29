print("What size would you like your game board?")
width = int(input("Width: "))
height = int(input("Height: "))

def drawBoard(x, y):
    for i in range(y):
        print('\n')
        for i in range(x):
            drawHorizontalUnit()
        print('\n')
        for i in range(x):
            drawVerticalUnit()
        drawVerticalUnit()
    print('\n')
    for i in range(x):
            drawHorizontalUnit()
    

def drawHorizontalUnit():
    print(" -----", end='')

def drawVerticalUnit():
    print("|     ", end='')


drawBoard(width, height)






