from hand import *
from deck import *
from card import *

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

##game = CardGame() 
##hand = OldMaidHand("frank") 
##game.deck.deal([hand], 13) 
##print hand
##hand.removeMatches()
##print hand


class OldMaidGame(CardGame):
    def play(self, names): 
        # remove Queen of Clubs 
        self.deck.removeCard(Card(0,12)) 

	# make a hand for each player 
	self.hands = [] 
	for name in names : 
	  self.hands.append(OldMaidHand(name)) 

	# deal the cards 
	self.deck.deal(self.hands) 
	print "---------- Cards have been dealt" 
	self.printHands() 

	# remove initial matches 
	matches = self.removeAllMatches() 
	print "---------- Matches discarded, play begins" 
	self.printHands() 

	# play until all 50 cards are matched 
	turn = 0 
	numHands = len(self.hands) 
	while matches < 25: 
	  matches = matches + self.playOneTurn(turn) 
	  turn = (turn + 1) % numHands 

	print "---------- Game is Over" 
	self.printHands()

    def removeAllMatches(self): 
	count = 0 
	for hand in self.hands: 
	  count = count + hand.removeMatches() 
	return count

    def playOneTurn(self, i): 
	if self.hands[i].isEmpty(): 
            return 0 
	neighbor = self.findNeighbor(i) 
	pickedCard = self.hands[neighbor].popCard() 
	self.hands[i].addCard(pickedCard) 
	print "Hand", self.hands[i].name, "picked", pickedCard 
	count = self.hands[i].removeMatches() 
	self.hands[i].shuffle() 
	return count 

    def findNeighbor(self, i): 
        numHands = len(self.hands) 
        for next in range(1,numHands): 
            neighbor = (i + next) % numHands 
            if not self.hands[neighbor].isEmpty(): 
                return neighbor

    def printHands(self):
        for hand in self.hands:
            print hand


