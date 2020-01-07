# File: hw7.py
# Author: Siril Pattammady
# Date: 10/31/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A series of excercises designed to help practice functions, and
# calling them to preform tasks  as needed. 
# Collaboration:
# I collaborated with Harsh Patel (harsh3@umbc.edu) he helped me understand
# passing parameters and functions.


def createIntList():

    integer_list = []
    SENTINEL = input("What do you want the sentinel to be?")

    value = int(input("Please enter a number," +SENTINEL+" to stop:"))

    while str(value) != SENTINEL:
        integer_list.append(value)
        value = int(input("Please enter a number,"+SENTINEL+" to stop:"))
    return integer_list


def getValidInt(minn,maxx):
    
    message = ("Please enter a number between " + str(minn) + " and " + str(maxx) + " (inclusive) : ")

    newInt =int(input(message))
    while newInt <  minn or newInt > maxx:
        newInt = int(input(message))

    return newInt
    
        
def printMenu():

    LIST = ("1 - Create a list")
    CHECK =  ("2 - Check if list is all the same")
    DIFF = ("3 - Check if list is all different")
    SORT = ("4 - Check if list is sorted")
    EXIT = ("5 - Exit the program" )

    print(LIST)
    print(CHECK)
    print(DIFF)
    print(SORT)
    print(EXIT)
    
def allTheSame(num_list):
    
    if num_list == []:
        num_list = [0]

    previous  = num_list[0]

    bool1 = True
    
    for i in num_list:
        if i != previous:
            bool1 = False
    return bool1

                
def allDifferent(num_list):


    bool1 = True
    num_list2 = num_list[:]
    for i in num_list:
        num_list2.remove(i)
        
        for n in num_list2:
            if i == n:
                bool1=False
                
    return bool1

def allsorted(num_list):

    if num_list == []:
        num_list = [1,2]
    next = num_list[0]-1
    
    bool1 = True
    
    for i in num_list:

        if i < next:
            bool1 = False
        next = i
            
    return bool1
            

def main():

    printMenu()

    choice = getValidInt(1,5)
    choice_1 = []
    while choice != 5:
        
        if choice == 1:
            choice_1 = createIntList()
            print()
            printMenu()
            print()
            choice = getValidInt(1,5)
        
        if choice == 2:
            same = allTheSame(choice_1)
            if same == True:
                statement = " is all the same elements"
            else:
                statement =" is not all the same elements"
            print("The list",choice_1,statement)
            print()
            printMenu()
            print()
            choice = getValidInt(1,5)
            
        if choice == 3:
            different = allDifferent(choice_1)
            if different == True:
                statement_2 = "is all unique elements"
            else:
                statement_2 = "is all the same elements"
            print ("The list", choice_1, statement_2)
            print()
            printMenu()
            print()
            choice = getValidInt(1,5)
            
        if choice == 4:
            sort = allsorted(choice_1)
            if sort == True:
                statement_3 = "is sorted"
            else:
                statement_3 = "is not in order"
            print("The list", choice_1, statement_3)
            print()
            printMenu()
            print()
            choice = getValidInt(1,5)
    if choice == 5:
        print("Thank You for using the List Info Checker")
main()

    
