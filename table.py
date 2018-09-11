#!/usr/bin/python3
from deck import Deck
import csv

class Table:
   
    player_bust = False
    new_hand = False
    hit_count = 0

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.d = Deck(1)
            
    def deal(self):
        self.player_hand.append(self.d.deck.get())
        self.dealer_hand.append(self.d.deck.get())
        self.player_hand.append(self.d.deck.get())
        self.dealer_hand.append(self.d.deck.get())
        self.print_hand(-1)
        self.print_hand(1)

    def deal_new_hand(self):
        self.d = Deck(1)
        self.new_hand = False
        self.clear_table()
        self.deal()
        self.player_bust = False
        self.hit_count = 0

    def print_hand_totals(self):
        print('Player\'s Hand: {} '.format(self.check_hand(self.player_hand)))

    def print_hand(self, turn, show=None):
        if turn  == 1:
            print('Player\'s Hand: ', end='')
            for i in self.player_hand:
                print('{}, '.format(i),end='')
            print(' -- {}'.format(self.check_hand(self.player_hand)))
        elif (show == True):
            print('Dealer\'s Hand: ', end='')
            for i in self.dealer_hand:
                print('{}, '.format(i),end='')
            print(' -- {}'.format(self.check_hand(self.dealer_hand)))
        else:
            print('Dealer\'s Hand: {}'.format(self.dealer_hand[1]))

    def clear_table(self):
        self.player_hand = []
        self.dealer_hand = []
                                                                          
    def hit(self):    
        #player's turn
        self.player_hand.append(self.d.deck.get())
        self.print_hand(1)
        self.hit_count += 1
        return self.check_bust(self.player_hand)

    def stand(self):
        while self.check_hand(self.dealer_hand) < 17 and self.check_bust(self.dealer_hand) > 0:
            self.dealer_hand.append(self.d.deck.get())
        self.record_handler()
        self.print_hand(-1, True)
        return self.check_winner()

    def check_hand(self, hand, limit=None):
        total = 0
        if limit != None:
            sorted_hand = sorted(hand[:limit+1], key=lambda x: (x is 'A', x))    
        else:
            sorted_hand = sorted(hand, key=lambda x: (x is 'A', x))
        for c in sorted_hand:
            if total >= 11 and c  == 'A':
                total += 1
            else:
                total += self.d.values[c]
        return total

    def check_bust(self, hand):
        if self.check_hand(hand) > 21:
            return -1
        else:
            return 1

    def check_winner(self):
        self.new_hand = True
        if self.check_bust(self.dealer_hand) > 0 and self.check_hand(self.dealer_hand) > self.check_hand(self.player_hand):
            return -1
        elif self.check_hand(self.dealer_hand) == self.check_hand(self.player_hand):
            return 0
        else:
            return 1

    def record_handler(self): 
        recorder = []
        print(self.hit_count)
        recorder.append(self.check_winner())
        for j in range(self.hit_count+1):
            if j == 0:
                recorder.append(self.dealer_hand[1])
                recorder.append(self.player_hand[0])
                recorder.append(self.player_hand[1])
                recorder.append(self.check_hand(self.player_hand, j+1))
            else:
                recorder.append('1')
                recorder.append(self.player_hand[j+1])
                recorder.append(self.check_hand(self.player_hand, j+2))
        with open('games.csv', 'a') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #dealerUpCard, card1, card2, hit1, card3, totalAfter3, hit2, card4, totalAfter4, hit3, card5, totalAfter5
            filewriter.writerow([recorder])
        return 0        
