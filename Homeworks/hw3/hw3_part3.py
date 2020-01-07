# File: hw3_part3.py
# Author: Siril Pattammady
# Date: 9/26/2016
# Section: SECTION 01
# E-mail: psiril1@umbc.edu
# Description:
# Obtain a temperature for Celsius or Kelvin and state whether water is
# a liquid, gas, or solid at that room temperature.
# Collaboration:
# I did not collaborate with anyone on this assignment.

def main():

    temp = float(input("Please enter the temperature:"))
    scale = input("Please enter 'C' for Celsius, or 'K' for Kelvin:")
    if scale== "C" and temp <= 0:
        print("At this temperature, water is a (frozen) solid.")
    elif scale == "C" and temp >= 100:
        print("At this temperature, water is a gas.")
    elif scale== "C" and temp > 0 and temp < 100:
        print("At this temperature, water is a liquid.")
    elif scale == "K" and temp <= 273.16:
        print("At this temperature, water is a (frozen) solid.")
    elif scale == "K" and temp >= 373.16:
        print("At this temperature, water is a gas.")
    elif scale == "K" and temp > 273.16 and temp < 373.16:
        print("At this temperature, water is a liquid.")
    else:
        print("You entered an invalid input")
        
                       
main()
