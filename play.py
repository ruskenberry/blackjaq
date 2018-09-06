#!usr/bin/python3
from deck import Deck
from table import Table

t = Table()
t.deal()

choice = "play"
count = 0

while choice != 'quit':
    if (count != 0 and t.new_hand == True) or t.player_bust == True:
        print("*************************************")       
        t.deal_new_hand()
    choice = input("Hit (H,h), Stand (S,s) ")#, Split (SS), Double (D), Surrender (Su) ") 
    if choice == 'H' or choice == 'h':
        #hit
        if t.hit() == -1:
            t.stand()
            t.player_bust = True
            print("Bust! -- House Wins")
    elif choice == 'S' or choice == 's':
        #stand
        winner = t.stand()
        if(winner == -1):
            print("House wins :(")
        elif (winner == 0):
            print("Push")
        else:
            print("You win! xD")
    elif choice == 'SS':
        #split
        print('Splitting')
    elif choice == 'D':
        #double down
        print('Doubling Down')
    elif choice == 'Su':
        #surrender
        print('Surrendering')
    elif choice == 'quit':
        #say goodbye
        print('Goodbye!')
    else:
        #command not recognized
        print('Error: Command not recognized')
    count += 1
