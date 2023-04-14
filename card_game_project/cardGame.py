import random

class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def toString(self):
        str = self.rank + " " + self.suit
        return str

def initDeck(deck):
    for suit in ['\u2663','\u2664','\u2665','\u2666']:
        for rank in ['2','3','4','5','6','7','8','9','10','J','Q','K','A']:
            card = Card(suit,rank)
            deck.append(card)
    return deck

def printDeck(deck):
    for card in deck:
        print(card.toString())

def drawHand(deck):
    hand = []
    for i in range(5):
        card = random.choice(deck)
        deck.remove(card)
        hand.append(card)
    return hand

def printHand(hand):
    print("Hand is: ")
    for card in hand: 
        print(card.toString())

def isFullHouse(hand):
    ranks = []
    for card in hand:
        thisCard = card

        ranks.append(thisCard.rank)

    rankSet = set(ranks)

# breakpoint()
    if (ranks.count(list(rankSet)[0])==2) and (ranks.count(list(rankSet)[1])==3):
        return True
    elif(ranks.count(list(rankSet)[0])==3) and (ranks.count(list(rankSet)[1])==2):
        return True
    else:
        return False


def main():
    count = 0
    while(1):

        count+=1
        deck = []
        deck = initDeck(deck)

        hand = drawHand(deck)
        

        if isFullHouse(hand):
            printHand(hand)
            break
    print("Hands dealt before full house: ")
    print(count)
    print("Full house probability was: " )
    print(1/count)

if __name__ == "__main__":
    main()