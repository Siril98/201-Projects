# File:    nums.py
# Started: by Dr. Gibson
# Author:  Siril Pattammady
# Date:    10/24/2016
# Section: SECTION NUMBER 06
# E-mail:  psiril1@umbc.edu 
# Description:
#   This file contains python code that uses functions to 
#   allow a user to get basic information about a number
#   they've entered.

MIN_VAL = -1000000
MAX_VAL =  1000000

# evenOrOdd() takes in a number and returns whether it's even or odd
# Input:      number, an integer
# Output:     a string -- either "even" or "odd" should be returned
def evenOrOdd(number):

    number = int(input("Please enter a number between", MIN_VAL, "and" ,MAX_VAL,"inclusive:"))

    if number % 2 == 0:
        return("even")
    else:
        return("odd")

    return(number)
                 
    ####################################################################
    # your function to determine if the number's even or odd goes here #
    ####################################################################


# posNegZero() takes in a number and returns its sign
# Input:      num, an integer
# Output:     a string -- either "negative", "positive", or "zero" 
#                         should be returned
def posNegZero(num):

    if num > 0:
        return("positive")
    elif num < 0:
        return(" negative")
    else:
        return("zero")

    return(num)

    ##########################################################
    # your function to determine the number's sign goes here #
    ##########################################################


# getValidInt() takes in a minn and maxx, and gets a number from the
#               user between those two numbers (inclusive)
# Input:      minn and maxx, two integers
# Output:     an integer, between minn and maxx inclusive
def getValidInt(minn, maxx):
    message = "Please enter a number between " + str(minn) + " and " + \
        str(maxx) + " (inclusive): "


    
    newInt = int(input(message))

    while newInt>MIN_VAL or newInt<MAX_VAL:
        
    #######################################
    # your code that loops until the user # 
    # enters a valid number goes here     #
    #######################################

    # while loop exited, return the user's choice
    return newInt




def main():

    print("Welcome to the number program!")

    # get a valid number from the user

    
    
    ##########################################################
    # your code to call the function getValidInt() goes here #
    # ** use the constants MIN_VAL and MAX_VAL in your call  #
    ##########################################################


    # call the posNegZero function and print out the result to the user
    string = posNegZero(num)
    #########################################################
    # your code to call the function posNegZero() goes here #
    #########################################################
    print("The number", userNum, "is", sign)

    evenOrOdd(number)

    # call the evenOrOdd function and print out the result to the user
    ########################################################
    # your code to call the function evenOrOdd() goes here #
    ########################################################
    print("The number", userNum, "is", result)

    # say goodbye and exit the program
    print("Thank you for using the number program!  Come again!")


main()


