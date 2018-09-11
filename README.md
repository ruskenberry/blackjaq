# blackjaq
Console Casino -- Blackjack, for neural net training/playing

Usage
-----

```
 
 # TODO: document more stuff
 # then...
 python3 play.py or python3 robo_play.py for random h/s
```

TODOs
-----
* Robo-player
* Split, Surrender, Double
* Gambling?


Implementation
-----

Serialization
-----

Training Set
-----
Hopefully will be generated from running play.py with a loop and some random hit/stand clicks 

Notes
-----
* What to record for the training set:
* win/loss
	* -1/0/1
* dealerUpcard
	* The card in the dealer's hand visible to all players
* card1
	* Value of the first card
* card2
	* Value of the second card
* initialPoints
	* Total points with the two cards
* hit1
	* Binary variable indicating if a hit was taken
* card3
	* Value of the third card
* pointsAfterCard3
	* Total points with three cards
* hit2
	* Binary variable indicating if a hit was taken
* card4
	* Value of the fourth card
* pointsAfterCard4
	* Total points with four cards
* hit3
	* Binary variable indicating if a hit was taken
* card5
	* Value of the fifth card
* pointsAfterCard5
	* Total points with five cardsnapshot of hand after each hit until stand (just the totals?)
