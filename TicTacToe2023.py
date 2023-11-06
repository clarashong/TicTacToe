# ******************************
# TicTacToe - Clara Hong 
# November 5 2023
# ******************************

def main():
    finished = False
    turn = 1
    p1icon = "o"
    p2icon = "x"
    grid = [[i * 3 + j for j in range (0,3)] for i in range (0,3)]
    # ADD LATER intro(grid)

    grid = [[" " for j in range (0,3)] for i in range (0,3)]
    while (not finished):
        if (turn == 1) :
            icon = p1icon
        else: 
            icon = p2icon
        grid = takeTurn(grid,icon)
        if (checkRow(grid) and checkCol(grid)) :
            finished = True
        turn += 1
        printGrid(grid)
    

def intro(grid) :
    print("Hello there player! Welcome to tic tac toe")
    player = -1
    while (player < 1) :
        player = input("How many players? ")
        if (player != 1 | player != 2) :
            print("Please choose only one or two players.")



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

            
            
    

if __name__ == "__main__":
    main()
