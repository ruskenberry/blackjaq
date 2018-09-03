#!usr/bin/python3
from deck import Deck

def printHand():
    print('Dealer\'s Hand: {}, H'.format(dealer_hand[0]))
    print('Your Hand: {}, {} '.format(player_hand[0], player_hand[1]))

def deal():
    player_hand.append(d.deck.get())
    dealer_hand.append(d.deck.get())
    player_hand.append(d.deck.get())
    dealer_hand.append(d.deck.get())

d = Deck()
player_hand = []
dealer_hand = []
deal()
printHand()
choice = "play"

while choice!= "quit":
    choice = input("Hit (H), Stand (S), Split (SS), Double (D), Surrender (Su) ")
    if choice == 'H':
        #hit
        print('Hitting')
        printHand()
    elif choice == 'S':
        #stand
        print('Standing')
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

   
