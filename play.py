#!usr/bin/python3
from deck import Deck
from table import Table

t = Table()
t.deal()

choice = "play"
turn = True
count = 0
winner = -3

while choice != 'quit':
    if (count != 0 and winner != -3) or winner == -2:
        print("*************************************")       
        t.new_hand = False
        t.clear_table()
        t.deal()        
        winner = -3
    choice = input("Hit (H), Stand (S), Split (SS), Double (D), Surrender (Su) ") 
    if choice == 'H':
        #hit
        print('Hitting')
        if t.hit() == -2:
            t.stand()
            winner = -2
    elif choice == 'S':
        #stand
        print('Standing')
        turn = False
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
