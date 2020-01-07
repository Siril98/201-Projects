# File: games.py
# Author: Siril Pattammady
# Date: 10/19/2016
# Section:SECTION NUMBER 06
# E-mail: psiril1@umbc.edu
# Description: A short program to help the user and their friends decide 
# what game to play. The program will print out the list of possible games
# and then everyone can vote on which game they would like to play.
# The program will close if someone enters "0" and will output the total votes.
# Collaboration: During lab, collaboration between
# students is allowed, although I understand I still
# must understand the material and complete the
# assignment myself.

def main():

    vote_list = []

    games = ["Twister", "Dodgeball", "Capture the Flag",
             "Hide and Seek", "Croquet", "Ring Toss", "Ping Pong"]
    for g in range(len(games)):
        print(g+1 ,"-", games[g])
    print()
    votes= int(input("What game would you like to play? 0 to quit:"))
    vote_list.append(votes)
    while votes!= (0):
        votes = int(input("What game would you like to play? (0 to quit):"))
        vote_list.append(votes)
        vote_2 = [0]*len(games)
    print()
    for v in vote_list:
        if v == 1:
            vote_2[0] = vote_2[0] + 1
        elif v == 2:
            vote_2[v-1] = vote_2[v-1] + 1
        elif v == 3:
            vote_2[v-1] = vote_2[v-1] + 1
        elif v == 4:
            vote_2[v-1] = vote_2[v-1] +1
        elif v == 5:
            vote_2[v-1] = vote_2[v-1] +1
        elif v==6:
            vote_2[v-1] = vote_2[v-1] + 1
        elif v==7 :
            vote_2[v-1] = vote_2[v-1] +1
    print()
    
    for j in range(0,7):
        print(games[j],"has",vote_2[j],"votes")
        
    
        
            
    
main()
