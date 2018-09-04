#!usr/bin/python3
from deck import Deck
from table import Table

t = Table()
t.deal()

choice = "play"
turn = True
count = 0
winner = -2

while choice != 'quit':
    if ((count != 0) and (t.check_hand(t.player_hand) >= 21 or t.check_hand(t.dealer_hand) >= 21)) or winner != -2:
        t.new_hand = False
        t.clear_table()
        t.deal()        
        winner = -2
    choice = input("Hit (H), Stand (S), Split (SS), Double (D), Surrender (Su) ") 
    if choice == 'H':
        #hit
        print('Hitting')
        t.hit()
    elif choice == 'S':
        #stand
        print('Standing')
        turn = False
        winner = t.stand()
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
