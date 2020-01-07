# File: proj1.py
# Author: Siril Pattammady
# Date: November 6, 2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# The program is the game connect 4 for two people.
# Collaboration:
# Collaboration is not allowed on this assignment.


# Global Constants
MIN_VAL = 5
PLY_1 = "x"
PLY_2 = "o"
EMPTY = "_"
# A function that prints the introduction screeen for the two players
# Input: It asks whether or not if they want to load a game or not.
# Input: If user enters "n" then the game will load.
# Input: If the user enters "y" then the user can make a file for saving
# Input:It also asks for the number of rows and columns they want on their board.
# Output: Returns the value of columns and rows to main.
# Output: If user enters "y" then it will ask the user to make a game file.

def load():

    print("Welcome to Connect Four")
    print("This game is for two players")
    welcome = input("Would you like to load a game (y/n)?")
    
    while welcome != ("n") and welcome != ("y"):
        welcome = input("Would you like to load a game (y/n)?")
        
    if welcome == ("n"):
        print("Please choose the number of rows:")
        rows = int(input("Please enter a number greater than or equal to " +str(MIN_VAL)+ " : "))
        
    while rows < MIN_VAL:
        rows = int(input("Please enter a number greater than or equal to "+ str(MIN_VAL)+ " : "))

    if welcome == ("n"):
        print("Please choose the number of columns:")
        columns = int(input("Please enter a number greater than or equal to "+ str(MIN_VAL)+ " : "))

    while columns < MIN_VAL:
        columns = int(input("Please enter a number greater than or equal to " + str(MIN_VAL)+ " : " ))

    

    return(rows,columns)

# A function that asks the choice for player one and two on where they want to
# put their piece in the board.
# Input: Players column choice for their piece (integer)
# Output: Returns the players column choice in main.
def player(turn,columns):
    
    
    if turn % 2 != 0 :
        # if choice is s else
        print("Player 1 what is your choice?")
        choice = int(input("Please choose a column to place your piece in (1-"+str(columns)+") or s to save : "))
        
        
        
    elif turn % 2 == 0:
        print("Player 2 what is your choice?")
        choice = int(input("Please choose a column to place your piece in(1-"+str(columns)+") or s to save : "))
        
    turn += 1
        
    return(choice)

# A function that places an 'x' or an 'o' into the column the players choose.
# Input: The players turn will change the piece placed into the board
# Output: 'x' or 'o' into grid based on player turn
def placement(turn,choice,final_grid,rows):

    
    # whose turn it is
    if turn % 2 != 0:
        piece = PLY_1
    else:
        piece = PLY_2

    
    for index in range(rows-1, -1, -1):
        
        if final_grid[index][choice-1] == EMPTY:
            final_grid[index][choice-1] = piece
            return
    if final_grid[index][choice-1] != EMPTY:
        print("The column is full, please pick another column")
    if final_grid != EMPTY:
        print("There was a draw!!")
    return


# Makes a list given column and row value
# Input: Takes in the rows and column number
# Output: Creates a list given the row and column value
def board(rows,columns):

    final_grid = []
    
    
    for i in range(0,rows):
        final_grid.append(["_"]*columns)

    return final_grid

# Makes a board given the column and row value
# Input: Takes in the row and column value
# Output: Displays the board given the users input for column and row.
def display(rows,columns,final_grid):
    
    space = ""
    for i in range(rows):
        for j in range(columns):
            space = space + final_grid[i][j] + " "
        print(space)
        space = ""

            
# A function that checks the horizontal row for a winner
# It compares each index to the next checking if they are the same.
# Outputs: The winner is player 1 or 2
def horizontal(rows,columns,final_grid):

    answer = "1"
    
    for i in range(rows):
        for j in range(columns-3):
            if final_grid[i][j] == final_grid[i][j+1] and final_grid[i][j] == final_grid[i][j+2] and final_grid[i][j]== final_grid[i][j+3]:
                
                if final_grid[i][j] == PLY_1:
                    answer = "The winner is Player 1"
                elif final_grid[i][j] == PLY_2:
                    answer = "The winner is Player 2"
    return answer
                    
# A function that checks the horizontal row for a winner.
# It compares each index going up the list to the next checking if they are the same.
# Range of rows is subtracted by 3 because it will go out of range/bounds
# Outputs: The winner is player 1 or 2
def vertical(rows,columns,final_grid):

    answer = "1"
    for i in range(rows-3):
        for j in range(columns):
            if final_grid[i][j] == final_grid[i+1][j] and final_grid[i][j] == final_grid[i+2][j] and final_grid[i][j] == final_grid[i+3][j]:
                
                if final_grid[i][j] == PLY_1:
                    answer = "The winner is Player 1"
                elif final_grid[i][j] == PLY_2:
                    answer = "The winner is Player 2"
    return answer
                
# A function that checks the diagonal row for a winner going diagonal right.
# The three in each of the for loops is to ensure that it will not go out of range when checking.
# Outputs: The winner is player 1 or 2
def diagonalRight(rows,columns,final_grid):

    answer = "1"
    for i in range(3, rows):
        for j in range(columns-3):
            
            if final_grid[i][j] == final_grid[i-1][j+1] and final_grid[i][j] == final_grid[i-2][j+2] and final_grid[i][j] == final_grid[i-3][j+3]:
                if final_grid[i][j] == PLY_1:
                    answer = "The winner is Player 1"
                elif final_grid[i][j] == PLY_2:
                    answer = "The winner is Player 2"
    return answer
                
# A function that checks the diagonal row for a winner going diagonal left.
# Outputs: The winner is player 1 or 2
def diagonalLeft(rows,columns,final_grid):

    answer = "1"
    for i in range(3, rows):
        for j in range(3, columns):
            if final_grid[i][j] == final_grid[i-1][j-1] and final_grid[i][j] == final_grid[i-2][j-2] and final_grid[i][j] == final_grid[i-3][j-3]:
                
                if final_grid[i][j] == PLY_1:
                    answer = "The winner is Player 1"
                elif final_grid[i][j] == PLY_2:
                    answer= "The winner is Player 2"
    return answer
                
def main():

    # loading funtion
    rows,columns = load()
    # function for the board
    final_grid = board(rows,columns)
    # function that displays the board
    display(rows,columns,final_grid)

    # answer markers
    a = "1"
    b = "1"
    c = "1"
    d = "1"

    choice = 1
    turn = 1
    # A loop that calls the function for players turn and where they want their piece to go in.
    # It consists of the functions that will print out the winner.
    
    while a == "1" and b == "1" and c == "1" and d == "1":
        choice = player(turn,columns)
        
        position =  placement(turn,choice,final_grid,rows)
        display(rows,columns,final_grid)
        turn += 1
        a = horizontal(rows,columns,final_grid)
        b = vertical(rows,columns,final_grid)
        c = diagonalRight(rows,columns,final_grid)
        d = diagonalLeft(rows,columns,final_grid)
    # Refers to all the check functions
    # If any of the original answer markers change then it will print out the winner
    # This was originally in my while loop, but decided it was an easy way to stop the loop when someone wins
    if a != "1":
        print(a)
    if b != "1":
        print(b)
    if c != "1":
        print(c)
    if d != "1":
        print(d)
    

    ##### Does the whole program one more time
    question = input("Would you like to play again (y/n)?")
    while question == "y":
        rows,columns = load()

        final_grid = board(rows,columns)

        display(rows,columns,final_grid)


        a = "1"
        b = "1"
        c = "1"
        d = "1"

        choice = 1
        turn = 1
        # A loop that calls the function for players turn and where they want their piece to go in.
        while a == "1" and b == "1" and c == "1" and d == "1":
            choice = player(turn,columns)
            position =  placement(turn,choice,final_grid,rows)
            display(rows,columns,final_grid)
            turn += 1
            a = horizontal(rows,columns,final_grid)
            b = vertical(rows,columns,final_grid)
            c = diagonalRight(rows,columns,final_grid)
            d = diagonalLeft(rows,columns,final_grid)
            if a != "1":
                print(a)
            if b != "1":
                print(b)
            if c != "1":
                print(c)
            if d != "1":
                print(d)

        question = input("Would you like to play again (y/n)?")
main()

    

