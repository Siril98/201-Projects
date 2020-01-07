# File: proj2.py
# Author: Siril Pattammady
# Date: 12/4/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A program that takes in a maze file from the user and will use recursion to
# find a path to the solution of the maze or return no solution if any.
# Collaboration:
# Collaboration was not allowed on this assignment

# Global Constants for right,down,left, and top wall
# Global constants for a dead end and empty space
RIGHT = 0
DOWN = 1
LEFT = 2
TOP = 3
END = 3
SPACE = 0

# Function that takes in the filename of the maze and opens it for reading
# Converts text file into a list
def openfile(filename):
    maze = []
    file_input = open(filename)

    # Access the file to read each line and appends each line to the empty list
    lines = file_input.readlines()
    for content in lines:
        content = content.strip()
        maze.append(content)
        
    # Takes in the rows and columns from text file and splits it on the space
    # Initialize the rows and column values as an integer
    dim = maze[0]
    rows,columns = dim.split(" ")
    rows = int(rows)
    columns = int(columns)

    # Removes the rows,columns,and finishing position from maze
    # Takes the coordinates of the row and column solution and splits it on the space
    # Initialize a variable for the coordinates as an integer
    dim2 = maze[1]
    final_r,final_c = dim2.split(" ")
    final_r = int(final_r)
    final_c = int(final_c)
    maze.remove(dim)
    maze.remove(dim2)

    # Joins the contents in the list
    for i in range(len(maze)):
        maze[i] = maze[i].split(" ")
        maze[i] = ("").join(maze[i])
    
    
    # A loop to access the row, its square, and the side.
    # Creating a 3-D list
    # For loop looks at the range of rows and columns to append in new empty list(new_maze) 
    new_maze = []
    count = 0
    for num in range(rows):
        new_maze.append(maze[num+count:num+columns+count])
        count += 3
    
           
    file_input.close()
    return(new_maze,rows,columns,final_r,final_c)

# Function that takes in users valid starting row and column for the particular maze:
# Input: Takes in integer input for starting rows and columns for position on maze
# Outputs: Prompts user to enter another value if it input is not a valid choice
def start(rows,columns):

    row_input = int(input("Please enter the starting row:"))
    # Takes in the user row input if it meets the condition(valid)
    while row_input < 0 or row_input > rows-1:
        row_input = int(input("Invalid, enter a number between 0 and "+ str(rows-1)+" (inclusive):"))
        
    # Takes in the user column input if it meets the condition (valid)
    column_input = int(input("Please enter the starting column: "))
    while column_input < 0 or column_input > columns-1:
                column_input = int(input("Invalid, enter a number between 0 and " + str(columns-1) + " (inclusive):" ))
    
    return(row_input,column_input)

# Function that checks the maze for a solution
# Input: User inputs in valid coordinate in the maze
# Output: Returns if there is a solution or not to the main
# Output: If there is a solution then it will print out the solution path
def check(new_maze,row_input,column_input,final_r,final_c,path):
    
    # BASE CASES
    # If user starts in a closed square return no solution found
    
    curr_point = new_maze[row_input][column_input]

    if int(new_maze[row_input][column_input][RIGHT])== 1 and int(new_maze[row_input][column_input][DOWN]) == 1 and int(new_maze[row_input][column_input][LEFT])== 1 and int(new_maze[row_input][column_input][TOP])== 1:
        print("No solution found!")
        return False 
    # If the user makes it to the end of the maze (solution) returns solution found
    if row_input == final_r:
        if column_input == final_c:
            print("Solution found!")
            return True

    
        
    # RECURSIVE CASES
    # Checks Right
    # If there is a space and current position is not in the list that takes in the path
    # Then moves right and appends current location to the list
    if int(new_maze[row_input][column_input][RIGHT]) == SPACE and (row_input,column_input+1) not in path :
           
        column_input+=1
        path.append((row_input,column_input))
        check(new_maze,row_input,column_input,final_r,final_c,path)
        return True
    
    # Checks down
    # If there is a space going down and current position is not in the list that takes in the path
    # Appends the current location if statment is true
    if int(new_maze[row_input][column_input][DOWN]) == SPACE and (row_input+1,column_input) not in path :
        row_input += 1
        path.append((row_input,column_input))
        check(new_maze,row_input,column_input,final_r,final_c,path)
        return True
        
    # Checks Left
    # If there is a space to the left and current position is not in the list that takes in the path
    # Appends current location to the path
    if int(new_maze[row_input][column_input][LEFT])== SPACE and (row_input,column_input-1) not in path :
       
        column_input -= 1
        path.append((row_input,column_input))
        check(new_maze,row_input,column_input,final_r,final_c,path)
        return True
        
    # Checks Up
    # If there is a space checking up and current position is not in the list that takes in the path
    # Appends current location to the path
    if int(new_maze[row_input][column_input][TOP])== SPACE and (row_input-1,column_input) not in path :
       
        row_input -= 1
        path.append((row_input,column_input))
        check(new_maze,row_input,column_input,final_r,final_c,path)
        return True
    
    # Back Tracking statement
    # When it reaches a dead end
    # If the sum of each side is 3 then you know the path is at a dead end
    # If the initial input is in the path list and not equal to the final coordinates (since the inputs are constantly changing)
        
    # Set the path back at the start position to find a new path
    # If the sum of all sides is equal to 3
    if int(new_maze[row_input][column_input][RIGHT]) + int(new_maze[row_input][column_input][DOWN]) + \
            int(new_maze[row_input][column_input][LEFT]) + int(new_maze[row_input][column_input][TOP]) == END:
        
        # If the current position is in the path and not equal to the final solution
        # Change the current position to the starting postion
        # Will recursively run the function again to find solution
        if (row_input,column_input) in path and row_input!= final_r and column_input != final_c:
            (row_input,column_input) = path[0]
            path.append((row_input,column_input))
      
            check(new_maze,row_input,column_input,final_r,final_c,path)
            return False

def main():
    # Path that takes in every checked place
    path = []
    # Copies of original path
    copy_path = []
    final_path = []
    
    print("Welcome to the Maze solver!")
    # Calls function to enter and open user file input
    filename = input("Please enter the filename of the maze:")
    new_maze,rows,columns,final_r,final_c = openfile(filename)
    
    # Calls function that takes in the users starting rows and columns.
    # Appends the user input to the path
    row_input,column_input = start(rows,columns)
    path.append((row_input,column_input))
    
    # Calls function that checks around the maze.
    search = check(new_maze,row_input,column_input,final_r,final_c,path)

    # Loop that takes in the path and only saves the path that finds the solution to a list
    index = -1
    while path[index] != (row_input,column_input):
        copy_path.append(path[index])
        index -= 1
    
    copy_path.append((row_input,column_input))
    
    # Second loop that takes in the copied loop of solution coordinates in the correct order
    index = -1
    
    while copy_path[index] != (final_r,final_c) and len(copy_path)!= 1:
        final_path.append(copy_path[index])
        index-=1
    final_path.append((final_r,final_c))
    
    # Loop that only prints coordinates of solved maze
    # If the length is 1 then there is no solution
    if len(final_path)!= 1:
        for coordinates in final_path:
            print(coordinates)
    
        
main()
