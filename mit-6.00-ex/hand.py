import deck
from card import *

class Hand(deck.Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def addCard(self, card):
        self.cards.append(card)

    def __str__(self):
        s = 'Hand ' + self.name
        if self.isEmpty():
            return s + " is empty\n"
        else:
            return s + " contains\n" + deck.Deck.__str__(self)


class OldMaidHand(Hand): 
    def removeMatches(self):
        count = 0
        originalCards = self.cards[:]
        for card in originalCards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print "Hand %s : %s matched %s" % (self.name, card, match)
                count = count + 1
        return count

    
