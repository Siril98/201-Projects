# File: hw3_part4.py
# Author: Siril Pattammady
# Date: 9/27/16
# Section: SECTION NUMBER 01
# E-mail: psiril1@umbc.edu
# Description:
# Creating a simplified day of the week calculator
# Collaboration:
# I did not collaborate with anyone on this assignment.

def main():

    date = int(input("Please enter the day of the month:"))
    if date == 1 or date==8 or date==15 or date==22 or date==29:
        print("Today is Sunday!")
    elif date == 2 or date == 9 or date == 16 or date == 23 or date==30:
        print(" Today is Monday!")
    elif date == 3 or date == 10 or date== 17 or date== 24:
        print("Today is Tuesday!")
    elif date == 4 or date== 11 or date == 18 or date==25:
        print("Today is Wednesday!")
    elif date == 5 or date==12 or date==19 or date==26:
        print("Today is Thursday!")
    elif date == 6 or date==13 or date==20 or date==27:
        print("Today is Friday!")
    elif date== 7 or date== 14 or date==21 or date==28:
        print("Today is Saturday!")
    else:
        print("The date" ,date,"is an invalid day")

main()
