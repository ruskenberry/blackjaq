#!/usr/bin/env python3
import random
import queue
class Deck:

    def __init__(self, num_of_decks=None):
        self.values = {'2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8,
                    '9' : 9, '10' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11 }
        self.deck_array = []
        self.deck = queue.Queue()
        if num_of_decks is None:
            num_of_decks = 1
        print('Initializing deck_array with {} decks'.format(num_of_decks))
        for x in range(0,num_of_decks):
            for val in self.values:
                self.deck_array.append(val)

        random.shuffle(self.deck_array)
        for d in self.deck_array:
            self.deck.put(d)
        #list(map(q.put, deck_array))


