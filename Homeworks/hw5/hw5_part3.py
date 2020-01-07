# Author: Siril Pattammady
# Date: 10/11/2016
# Section: SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description:
# A program that prints the number from 101 down to 1 inclusively.
# There are three special cases where it would print a message.
# Collaboration:
# I did not collaboate with anyone on this assignment.


def main():


    for n in range(101,0,-1):
        if n % 5 == 0 and n%6==0:
            print("Thirty days hath September.")
        elif n%5==0 or n%6==0:
            if n%5==0:
                print("Where do you see yourself in five years? ")
            else:
                print("I'll believe six impossible things before breakfast. ")
        else:
            print(n)

    
main()
