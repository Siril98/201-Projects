# File: hw6.py
# Author: Siril Pattammady
# Date: 10/25/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A series of excercises to help practice functions. The program wil take in
# an inputs that will be put in a list. In the list the program will print the
# list,summation and product of all the values inputted. The user can also input
# the amount of lists they want to have.
# Collaboration:
# Collaboration was not allowed on this assignment.


def summation(integer_list):
    
    summation = 0
    
    for a in integer_list:
        summation = a + summation
    return(summation)
     
def multiply(integer_list):

    product = 1

    for b in integer_list:
        product = b * product
    return(product)

def createIntList(list_1):
    
    integer_list = []
    print("You are creating list #",list_1 + 1 )
    SENTINEL = input("What do you want the sentinel to be?:")



    value = int(input("Please enter a number,"+ SENTINEL + " to stop:"))
    while str(value)!= SENTINEL:
        integer_list.append(value)
        print(value)
        value = int(input("Please enter a number,"+ SENTINEL + " to stop:"))
        
    return(integer_list)

def main():    

    LIST = int(input("How many lists would you like to create?:"))

    for r in range(LIST):
        
        list_total = createIntList(r)
        print("For the list",list_total)
    
        add_total = summation(list_total)
        print("The summation is",add_total)

        mult_total = multiply(list_total)
        print("The product is",mult_total)

    print("Thank you for using the Simple Math Helper")
    
main()
