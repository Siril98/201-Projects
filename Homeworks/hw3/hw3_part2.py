# File: hw3_part2.py
# Author: Siril Pattammady
# Date: 9/26/2016
# Section: SECTION NUMBER 01
# E-mail: psiril1@umbc.edu
# Description:
# A simple game that determines/guesses a dog's breed.
# Collaboration:
# I did not collaborate on this assignment.

def main():
    print("Please enter 'yes' or 'no' to these questions.")
    big_dog = input("Is the dog a big dog?:")
    if big_dog =="yes":
        fluffy_coat =input("Does the dog have a fluffy coat?:")
        if fluffy_coat =="yes":
            print("Your dog is a Samoyed")
        else:
            ears_stick_up = input("Does the dog's ears stick up?:")
            if ears_stick_up == "yes":
                print("Your dog is a German Shepherd")
            else:
                print("Your dog is a Borzoi")
    else:  
      curly_tail = input("Does the dog have a curly tail?:")
      if curly_tail == "yes":
        print("Your dog is a Shiba Inu")
      else:
        print ("Your dog is a Corgi")
main()
