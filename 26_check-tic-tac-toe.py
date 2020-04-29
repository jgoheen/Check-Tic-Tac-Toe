import random
from random import randint

def printMatrix(matrix):
    x = 0
    for x in range(3):
        print(matrix[x])
        x += 1

def checkForWinner(matrix):
    # check horizontal
    i = 0
    j = 0
    for x in range(3):
        if ((matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]) and matrix[i][j] != 0):
            print("winner row ", i, ", Player: ", matrix[i][j])
        i += 1

    # check vertical
    i = 0
    j = 0
    for y in range(3):
        if ((matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]) and matrix[i][j] != 0):
            print("winner column ", j, ", Player: ", matrix[i][j])
        j += 1

    # check diagonal
    i = 0
    j = 0
    if ((matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2]) and matrix[i][j] != 0):
        print("winner whack, player: ", matrix[i][j])
    i = 0
    j = 0
    if ((matrix[i][j+2] == matrix[i+1][j+1] == matrix[i+2][j]) and matrix[i][j] != 0):
        print("winner slash, Player: ", matrix[i][j+2])         

board = [[0,0,0],[0,0,0],[0,0,0]]
i = 0
j = 0

for x in range(3):
    for y in range(3):
        board[i][j]=randint(0,2)
        j += 1
    i += 1
    j=0

printMatrix(board)
checkForWinner(board)



