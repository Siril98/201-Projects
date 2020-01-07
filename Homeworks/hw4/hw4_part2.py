# File: hw4_part2.py
# Author: Siril Pattammady
# Date: 10/03/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A program that computes the modulus without using the mod operator.
# Collaboration:
# Collaboration is not allowed on this assignment.

def main():

    num1 = float(input("Please enter the first number:"))
    num2 = float(input("Please enter the second number:"))
    mod = num1-num2
    while mod > num2:
        mod= mod-num2
    
    print(mod)
                     
    
main()
