# File:    semester.py
# Started: by Dr. Gibson
# Author:  Siril Pattammady
# Date:    10/03/2016
# Section: SECTION NUMBER 06
# E-mail:  psiril1@umbc.edu 
# Description:
#   This file contains python code that asks the user for their
#   courses, then goes through the list and asks them for their
#   raw grade for each course, removes the course from the list, 
#   and calculates and prints their average grade for the semester.

def main():

    # constant for the sentinel value, and an empty list to start
    COURSE_SENTINEL = "NONE"
    courseList = []

    # populate the course list
    course = input("What course did you take? ('NONE' to stop): ")
    while course!=("NONE"):
        
    #### YOU NEED TO PUT A WHILE LOOP HERE
    
        # save the course and ask for another
        courseList.append(course)
        course = input("What course did you take? ('NONE' to stop): ")
    
    # create variables to help calculate the student's average
    gradeList = []
    total = 0
    grade = int(input("What raw grade did you get in?"+ courseList[0]))
    while len(courseList)>0:
        gradeList.append(grade)
    grade = int(input("What raw grade did you get in?"+ courseList[0]))
    courseList.remove(courseList[0])
    total = total + grade
    print("In the",len(courseList),"you took, you recieved a" ,total,"as your average raw grade.")             
                

    # go through the course list; continue while the list is not empty
    
        # ask about their grade for each course and save it to the total
         
        # remove() the course from the list


    # calculate their average raw grade
    

    # print out their average raw grade


main()
