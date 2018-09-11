#!usr/bin/python3
#robo play
from deck import Deck
from table import Table
from random import randint


t = Table()
t.deal()

choice = "play"
count = 0

while True:
    if (count != 0 and t.new_hand == True) or t.player_bust == True:
        print("*************************************")       
        t.deal_new_hand()
    choice = randint(0, 1) 
    if choice == 0:
        #hit
        if t.hit() == -1:
            t.stand()
            t.player_bust = True
            print("Bust! -- House Wins")
    elif choice == 1:
        #stand
        winner = t.stand()
        if(winner == -1):
            print("House wins :(")
        elif (winner == 0):
            print("Push")
        else:
            print("You win! xD") 
    count += 1
