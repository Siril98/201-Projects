# File:    capitals.py
# Started: by Dr. Gibson
# Author:  Siril Pattammady
# Date:    November 14, 2016
# Section: SECTION NUMBER 06
# E-mail:  psiril1@umbc.edu
# Description:
#   This file contains python code that reads in a list of
#   states and their capitals, stores it in a dictionary,
#   and then allows the user to list all options (states),
#   or to show the capital of a specified state.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself. 

QUIT     = "exit"
SHOW_ALL = "list"


# convertToDict() takes in the filename and converts to a dict
# Input:          a file object
# Output:         a dictionary containing the file contents
def convertToDict(fileContents):
    dict1 = {}
    
    # write the rest of the function (including the return)

    readFile = fileContents.readlines()
    for content in readFile:
        newFile = content.split(",")
        newFile2= newFile[1].strip()
        dict1[newFile[0]] = newFile2 

    return(dict1)
        
    
    

def main():

    stateCapFile = open("stateCaps.txt")
    # a function call to convertToDict goes here
    dict1 = convertToDict(stateCapFile)
    
    stateCapFile.close()

    QUIT = "quit"
    SHOW_ALL = "list"
    print("Welcome to the State Capital Lookup System")
    # message with all the prompts for the user
    msg = "\n\tPlease enter the state you want the capital of.\n" + \
        "\t(Use '" + SHOW_ALL + "' for choices, or '" + \
        QUIT + "' to quit): "

    choice = input(msg)

    # this should be a while loop that runs until the user chooses to "exit"
    # MAKE SURE TO USE THE CONSTANTS DEFINED AT THE TOP OF THE FILE!!!

        # inside the loop: if the user enters "list", show all the states

        # inside the loop: otherwise; check if the state exists

            # if the state exists, print its capital

            # otherwise, print that it is not a state


        # at the end of the while loop, get a new user input
    while choice != QUIT:
        if choice == SHOW_ALL:
            print(dict1)
            choice = input(msg)
        elif choice in dict1 == True:
            print(choice)
        else:
            print("Thank you for using the State Capital Lookup System!")
main()

    

