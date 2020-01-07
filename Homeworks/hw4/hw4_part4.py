# File: hw4_part4.py
# Author: Siril Pattammady
# Date: 10/03/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A code that stimulates the up and down movement of a hailstone in a storm.
# Collaboration:
# Collaboration is not allowed on this assignment.

def main():

    height = int(input("Please enter the starting height of the hailstone:"))

    while height!= 1:
        
        if height%2 == 0:
            print("Hail is currently at height", height/2,)
            height=(height/2)
        else:
            print("Hail is currently at height",height*3 + 1,)
            height=(height*3+1)
            
    print("Hail stopped at height 1")
        
            
            




    
main()
