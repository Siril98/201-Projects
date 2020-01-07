# File: hw3_part1.py
# Author: Siril Pattammady
# Date: 9/26/2016
# Section: Section 01
# E-mail: psiril1@umbc.edu
# Description:
# Prints out the number and wheter it is positive,negative, or equal to zero
# Collaboration:
# I did not collaborate with anyone on this assignment.

def main():
    
    num = float(input("Please enter a floating point number:  "))
    if num == 0:
        print("The number",num, "is equal to zero")
    elif num > 0:
        print("The number",num,"is positive")
    elif num < 0:
        print("The number",num,"is negative")

main()
