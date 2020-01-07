# File:        graduation.py
# Author:      Siril Pattammady
# Date:        11/7/2016
# Section:     YOUR SECTION NUMBER
# E-mail:      psiril1@umbc.edu
# Description: This assignment will seperate and iterate through each file for a students
#              first, last name, and their major.
# Collaboration: During lab, collaboration between students is allowed,
#                although I understand I still must understand the material
#                and complete the assignment myself.


def main():

    rosterFile = open("roster.txt", "r")
    anouncements = open("announcements.txt", "w")
    student_list = rosterFile.readlines()

    for i in range(len(student_list)):
        split_list = student_list[i].split(";")
       # strip_list = split_list.strip()
        #anouncements.write(strip_list[3] + strip_list[2]+" graduating with a degree in "+ strip_list[1])
       # anouncements.write("\n")
        anouncements.write(split_list[3] + split_list[2] + " graduating with a degree in " + split_list[0])
        anouncements.write("\n")

        
    
        
    rosterFile.close()
    anouncements.close()




    
main()
