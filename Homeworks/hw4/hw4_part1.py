# File: hw4_part4.py
# Author: Siril Pattammady
# Date: 10/02/2016
# Section: Section 06
# E-mail: psiril1@umbc.edu
# Description:
# Program that re-prompts the user until they produce a username that is at least
# 4 characters long, and no more than 12 characters long.
# Collaboration:
# Collaboration is not allowed on this assignment.

def main():
    index=4
    index_2=11
    user_name = input("Please enter username:")
    while index>len(user_name):
        print("That username is too short")
        print("The username must be between 4 and 12 characters.")
        user_name = input("Please enter another username:")
        user_name=user_name
    while index_2<len(user_name):
        print("That username is too long")
        print("The username must be between 4 and 12 characters.")
        user_name = input("Please enter another username:")
        if index> len(user_name):
            print("That username is too short")
            print("The username must be between 4 and 12 characters")
            user_name = input("Please enter another username:")
            user_name = user_name
    else:
        print("Thank you for choosing the username:",user_name,)
main()
