# File: hw2_part3.py
# Author: Siril Pattammady
# Date: 9/19/2016
# Section: SECTION 01
# E-mail: psiril1@umbc.edu
# Description:
# Basic Shopping List
# Collaboration:
# Collaboration is not allowedd on this assignmnet.

def main():
    item1=input("What would you like to buy first?")
    print("You are buying",item1)
    amount1 = int(input("How many would you like to buy?:"))
    item2 = input("What would you like to buy second?")
    print("You are buying:",item2)
    amount2 = int(input("How many would you like to buy?: "))
    item3 = input("What would you like to buy third?")
    print("You are buying: ",item3)
    amount3 = int(input(" How many would you like to buy?:"))
    totalNumber = amount1+amount2+amount3
    print("You are buying",totalNumber,"items:")
    print(amount1,item1)
    print(amount2,item2)              
    print(amount3,item3)
main()
