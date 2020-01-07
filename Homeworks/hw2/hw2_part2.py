# File: hw2_part2.py
# Author: Siril Pattammady
# Date: 9/19/2016
# Section: Section 1
# E-mail: psiril1@umbc.edu
# Description: How to extract the number of dollars and number
# of cents from a price when the price is given as a float. 
# Collaboration:
# Collaboration on this assignment is not allowed.

def main():

    Price = float(input(" What is the price?:$"))
    Dollars = int(Price)
    numCents = int((Price-Dollars)*100)
    print(" The number of dollars is: ", Dollars)
    print(" The number of cents is: ", numCents)

main()


   
