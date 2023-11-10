# ******************************
# TicTacToe - Clara Hong 
# Start: November 5 2023
# ******************************
import random
numPlayers = 1

def main():
    # starting variables
    finished = False
    turn = 1 # odd numbered turns are p1, even are p2
    p1icon = "o"
    p2icon = "x"
    currPlayer = 1

    # creating a 3x3 grid for the game
    grid = [[i * 3 + j for j in range (0,3)] for i in range (0,3)]
    # making a legend guide for square indexes
    grid = createLegend(grid)
    #introduction for the players 
    intro(grid)
    # filling all spaces in grid with " " (empty)
    grid = [[" " for j in range (0,3)] for i in range (0,3)]

    # gameplay
    while (not finished):
        # turn = odd, player 1
        # turn = even, player 2
        if (turn % 2 == 1) :
            icon = p1icon 
            currPlayer = 1   
        else: 
            icon = p2icon
            currPlayer = 2
        print("Player {}, your turn.".format(currPlayer))
        if (numPlayers == 1 and currPlayer == 2) : 
            chooseSquare(grid, icon)
        else: 
            takeTurn(grid, icon)

        # check to see if anyone has won, otherwise, continue on
        if (checkRow(grid) or checkCol(grid) or checkDiag(grid)) :
            finished = True
            printGrid(grid)
            print("We have a winner!")
            print("Player {} has won the game!".format(currPlayer))
        elif (checkTie(grid)): 
            finished = True
            printGrid(grid)
            print("It's a tie!")
        else :
            turn += 1
            printGrid(grid)

    # Ending 
    print("Thanks for playing!")
    exit(); 
            
# intro(grid) introduces the player(s) to the game, asks for the amount of players (1 or 2),
# and shows them the numbering system. 
def intro(grid) :
    print("Hello there! Welcome to tic tac toe")
    player = -1
    correctType = False
    while (not correctType) :
        correctType = True
        # making sure user input is an int that's one or 2
        try:
            player = int(input("How many players? "))
        except (ValueError): 
            # incorrect input has been given
            correctType = False
            print ("Please try again, choose either 1 or 2.")
        if (player == 1 or player == 2) :
            correctType = True
            numPlayers = player
            print("Let's get started!")
        else: 
            correctType = False
            player = -1
            print("Please choose only 1 or 2.")

    # print grid with the numbering system   
    print("Here is the grid, and the corresponding number for each square!")
    printGrid (createLegend(grid))


# printGrid (grid) will produce a tic tac toe 3X3 grid
# Takes a 2D list 
def printGrid(grid): 
    print("--+-+--") # horizontal divider
    for row in grid :
        print("|", end = '') # vertical divider
        for col in row: 
            print(col + "|", end = '')
        print(); 
        print("--+-+--")

# takeTurn(grid,icon) lets player choose a square on the grid and updates the game grid
# takeTurn: 2d list, String -> 2d list (updated)
# requires 2d list to be 3x3
def takeTurn(grid, icon):
    valid = False
    # while there is no valid player input
    while (not valid): 
        correctType = False
        # making sure input is an int between 0 and 8
        while (not correctType) :
            correctType = True
            try:
                spot = int(input("Choose a grid number: "))
            except (ValueError): 
                correctType = False

        if (spot >= 0 and spot <= 8): 
            if (grid[spot // 3][spot % 3] == " "):
                valid = True
                grid[spot // 3][spot % 3] = icon
                return grid
            else:
                valid = False
                print("Sorry, that space is already taken.")

# chooseSquare(grid,icon) chooses a random tile in the grid for the computer to make their play
# chooseSquare: 2d list, String -> 2d list
def chooseSquare(grid, icon) : 
    listNum = [0,1,2,3,4,5,6,7,8] 
    valid = False
    num = 0
    while (not valid) : 
        num = random.choice(listNum)
        if (grid[num // 3][num % 3] == " ") : 
            valid = True
            grid[num // 3][num % 3] = icon
    print("The computer chose {}".format(num))
    return grid


# checkRow(grid) checks whether a row has three of the same icons (not spaces)
# checkRow: 2d list -> Boolean
def checkRow(grid) :
    for i in range (0,3):
        starting = grid[i][0]
        if (grid[i][1] == starting and grid[i][2] == starting and starting != " "): 
            return True 
    return False 

# checkCol(grid) checks whether a column has three of the same icons (not spaces)
# checkCol: 2d list -> Boolean       
def checkCol(grid) :
    for i in range (0,3): 
        starting = grid[0][i]
        if (grid[1][i] == starting and grid[2][i] == starting and starting != " "): 
            return True
    return False

# checkDiag(grid) checks for three in a row for diagonals
# checkDiag: 2d list -> Boolean
def checkDiag(grid) :
    starting = grid[0][0]
    if (grid[1][1] == starting and grid[2][2] == starting and starting != " "): 
            return True
    starting = grid[0][2]
    if (grid[1][1] == starting and grid[2][0] == starting and starting != " "): 
            return True
    return False

# checkTie(grid) checks whether every space is filled on the grid
# checkTie: 2d list -> Boolean
def checkTie(grid) :
    for i in grid: 
        for j in i: 
            if (j == " ") :
                return False
    return True

def createLegend(grid) :
    for i in range (0,3) :
        for j in range (0,3) : 
            grid[i][j] = str(i * 3 + j)
    return grid

if __name__ == "__main__":
    main()
