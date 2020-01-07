# File: hw4_part3.py
# Author: Siril Pattammady
# Date: 10/03/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A more sophisticated version of the username length checker from Part 1
# Collaboration:
# Collaboration is not allowed on this assignment.

def main():

    username = input("Please enter your username :")
    short = 2
    big = 8
    length = len(username)
    index = username[-1]
    while short>length or big<length or index!="1":
        if short>length:
            print("Username is too short, it must be at least 2 characters long.")
        elif big<length:
            print("Username is too long, must be no longer than 8 characters long.")
        else:
            print("Username under 8 characters must end with a '1'")
        username = input("Please enter your username :")
        length = len(username)
        index = username[-1]
    
    print("Thank you for choosing the username",username)
            
        

    
    
main()
