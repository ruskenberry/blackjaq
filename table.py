#!/usr/bin/python3
from deck import Deck

class Table:
   
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.d = Deck(6)
            
    def deal(self):
        self.player_hand.append(self.d.deck.get())
        self.dealer_hand.append(self.d.deck.get())
        self.player_hand.append(self.d.deck.get())
        self.dealer_hand.append(self.d.deck.get())
        self.print_hand(-1)
        self.print_hand(1)
        #self.print_hand_totals()

    def print_hand_totals(self):
        #print('Dealer\'s Hand: {} '.format(self.check_hand(self.dealer_hand)))
        print('Player\'s Hand: {} '.format(self.check_hand(self.player_hand)))

    def print_hand(self, turn):
        if turn  == 1:
            print('Player\'s Hand: ', end='')
            for i in self.player_hand:
                print('|{}|'.format(i),end='')
            print(' -- {}'.format(self.check_hand(self.player_hand)))
        else:
            print('Dealer\'s Hand: ', end='')
            #for i in self.dealer_hand:
            print('|{}||'.format(self.dealer_hand[0]),end='')
            print() 

    def clear_table(self):
        self.player_hand = []
        self.dealer_hand = []
                                                                          
    def hit(self):    
        #player's turn
        self.player_hand.append(self.d.deck.get())
        self.print_hand(1) 
        #self.print_hand_totas()

    def stand(self):
        while self.check_hand(self.dealer_hand) <= 17:
            self.dealer_hand.append(self.d.deck.get())
            self.print_hand(-1)
            #self.print_hand_totals()
        return self.check_winner()

    def check_hand(self, hand):
        total = 0
        for c in hand:
            total += self.d.values[c]
        return total

    def check_winner(self):
        if self.check_hand(self.dealer_hand) > self.check_hand(self.player_hand):
            return -1
        elif self.check_hand(self.dealer_hand) == self.check_hand(self.player_hand):
            return 0
        else:
            return 1
