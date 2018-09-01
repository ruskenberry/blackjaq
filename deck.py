#!/usr/bin/python3
import random
class Deck:
    def __init__(self):
        self.values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
                    '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11 }
        self.shoe = []
        for x in range(0,4):
            for val in self.values:
                self.shoe.append(val)


        random.shuffle(self.shoe)
    

d = Deck()       
print('Card 1: {}'.format(d.shoe[0]))
print('Card 2: {}'.format(d.shoe[1]))
