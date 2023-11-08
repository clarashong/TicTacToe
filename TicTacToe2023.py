# ******************************
# TicTacToe - Clara Hong 
# November 5 2023
# ******************************

def main():
    # starting variables
    finished = False
    turn = 1 # odd numbered turns are p1, even are p2
    p1icon = "o"
    p2icon = "x"

    # creating a 3x3 grid for the game
    grid = [[i * 3 + j for j in range (0,3)] for i in range (0,3)]
    # making a legend guide for square indexes
    grid = createLegend(grid)
    #introduction for the players 
    intro(grid)
    grid = [[" " for j in range (0,3)] for i in range (0,3)]
    printGrid(grid)
    while (not finished):
        if (turn % 2 == 1) :
            icon = p1icon    
        else: 
            icon = p2icon
        print("Player {}, your turn.".format(turn % 2))
        grid = takeTurn(grid,icon)
        if (checkRow(grid) or checkCol(grid) or checkDiag(grid)) :
            finished = True
            printGrid(grid)
            print("We have a winner!")
            print("Player {} has won the game!".format(turn % 2))
        elif (checkTie(grid)): 
            finished = True
            printGrid(grid)
            print("It's a tie!")
        else :
            turn += 1
            printGrid(grid)
            
    print("Thanks for playing!")
            
    

def intro(grid) :
    print("Hello there! Welcome to tic tac toe")
    player = -1
    while (player < 1) :
        player = input("How many players? ")
        if (player != 1 | player != 2) :
            print("Please choose only one or two players.")
    print("Here is the grid, and the corresponding number for each square!")



#(printGrid grid) will produce a tic tac toe 3X3 grid
#Takes a 2D list 
def printGrid(grid): 
    print("--+-+--")
    for row in grid :
        print("|", end = '')
        for col in row: 
            print(col + "|", end = '')
        print(); 
        print("--+-+--")

def takeTurn(grid, icon):
    valid = False
    while (not valid): 
        correctType = False
        while (not correctType) :
            correctType = True
            try:
                spot = int(input("Give a grid coordinate number: "))
            except (ValueError): 
                correctType = False

        if (spot >= 0 and spot <= 8): 
            if (grid[spot // 3][spot % 3] == " "):
                valid = True
                grid[spot // 3][spot % 3] = icon
                return grid
        
def checkRow(grid) :
    for i in range (0,3): 
        starting = grid[i][0]
        if (grid[i][1] == starting and grid[i][2] == starting and starting != " "): 
            return True
    return False 
        
def checkCol(grid) :
    for i in range (0,3): 
        starting = grid[0][i]
        if (grid[1][i] == starting and grid[2][i] == starting and starting != " "): 
            return True
    return False

def checkDiag(grid) :
    starting = grid[0][0]
    if (grid[1][1] == starting and grid[2][2] == starting and starting != " "): 
            return True
    starting = grid[0][2]
    if (grid[1][1] == starting and grid[2][0] == starting and starting != " "): 
            return True
    return False

def checkTie(grid) :
    for i in grid: 
        for j in i: 
            if (j == " ") :
                return False
    return True

def createLegend(grid) :
    for i in range (0,3) :
        for j in range (0,3) : 
            grid[i][j] = i * 3 + j
    return grid

            
            
    

if __name__ == "__main__":
    main()
