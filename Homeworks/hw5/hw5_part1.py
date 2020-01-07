# File: hw5_part1.py
# Author: Siril Pattammady
# Date: 10 /10/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# Prompt the user for two integers in order to make a modulus table
# and the second integer is for how high you want the table to go.
# Collaboration:
# I did not collaborate with anuone on this assignment.


def main():

    num_1 = int(input("Please enter the number to mod by:"))
    num_2 = int(input("Please enter how high you'd like to go:"))

    for num in range(num_2+1):
        mod = (num%num_1)
        print (num,"%",num_1,"=",mod,)
    
main()        
        
