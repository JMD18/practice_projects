import random
import numpy as np
import matplotlib.pyplot as plt

class Card:
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def toString(self):
        output = self.rank + " " + self.suit + " " + str(self.value)
        return output

def initDeck(deck):
    value = 1
    for suit in ['\u2663','\u2664','\u2665','\u2666']:
        for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
            card = Card(suit,rank,value)
            deck.append(card)
            value += 1
    return deck

def initLargeDeck(deck):
    value = 1
    for i in range(2):
        for suit in ['\u2663','\u2664','\u2665','\u2666']:
            for rank in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
                card = Card(suit,rank,value)
                deck.append(card)
                value += 1
    return deck

def printDeck(deck):
    for card in deck:
        print(card.toString())

    pass


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
    
    pass

# def isFullHouse(hand):
#     ranks = []
#     for card in hand:
#         thisCard = card

#         ranks.append(thisCard.rank)

#     rankSet = set(ranks)

#     pass

# # breakpoint()
#     if (ranks.count(list(rankSet)[0])==2) and (ranks.count(list(rankSet)[1])==3):
#         return True
#     elif(ranks.count(list(rankSet)[0])==3) and (ranks.count(list(rankSet)[1])==2):
#         return True
#     else:
#         return False
    
# def calculateFullHouse():

#     count = 0
#     while(1):

#         count+=1
#         deck = []
#         deck = initDeck(deck)

#         hand = drawHand(deck)
        

#         if isFullHouse(hand):
#             printHand(hand)
#             break
#     print("Hands dealt before full house: ")
#     print(count)
#     print("Full house probability was: " )
#     print(1/count)

#     pass

def deckAsValues(deck):

    values = []

    for card in deck:
        values.append(card.value)

    # print(values)

    return values


def binaryShuffle1(deck):

    newDeck = []
    median = (int)(len(deck)/2)

    for i in range(median):
        newDeck.append(deck[i])
        newDeck.append(deck[i+median])
    
    deck = newDeck

    # print("new shuffle")
    # printDeck(deck)

    return deck


def firstRun():

    deck = []
    initDeck(deck)
    # printDeck(deck)

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
    ax.title.set_text('Correlation for Run 1')
    ax.set(xlabel='Number of Shuffles',ylabel='R-Value')
    ax.scatter(0,1)
    print("Example output for Run 1: \n" )

    for i in range(16):
        deck = binaryShuffle1(deck)
        rho = find_R_value(deck)

        ax.scatter([i+1],rho)     
        print("Shuffle Number: " + str(i+1) + " | R-Value : " + str(rho))

    fig.subplots_adjust(wspace=.4)    
    plt.show()

    pass


def binaryShuffle2(deck):

    newDeck = []
    median = (int)(len(deck)/2)

    for i in range(median):
        newDeck.append(deck[i+median])
        newDeck.append(deck[i])
    
    deck = newDeck
    
    return deck


def secondRun():

    deck = []
    initDeck(deck)
    # printDeck(deck)

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
    ax.title.set_text('Correlation for Run 2')
    ax.set(xlabel='Number of Shuffles',ylabel='R-Value')
    ax.scatter(0,1)
    print("Example output for Run 2: \n" )

    for i in range(15):
        deck = binaryShuffle2(deck)
        rho = find_R_value(deck)

        ax.scatter([i+1],rho)             
        print("Shuffle Number: " + str(i+1) + " | R-Value : " + str(rho))

    fig.subplots_adjust(wspace=.4)    
    plt.show()

    # print(find_R_value(deck))
    pass

def thirdRun():

    deck = []
    deck2 = []
    initLargeDeck(deck)
    initLargeDeck(deck2)

    # print(deckAsValues(deck))
    deck.append(deck2)

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
    ax.title.set_text('Correlation for Run 3')
    ax.set(xlabel='Number of Shuffles',ylabel='R-Value')
    ax.scatter(0,1)
    print("Example output for Run 3: \n" )

    for i in range(15):
        deck = binaryShuffle1(deck)
        rho = find_R_value(deck)
        ax.scatter([i+1],rho)     
        print("Shuffle Number: " + str(i+1) + " | R-Value : " + str(rho))

    fig.subplots_adjust(wspace=.4)    
    plt.show()

    pass

def fourthRun():

    deck = []
    deck2 = []
    initLargeDeck(deck)
    initLargeDeck(deck2)

    # print(deckAsValues(deck))
    deck.append(deck2)

    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(12, 5))
    ax.title.set_text('Correlation for Run 4')
    ax.set(xlabel='Number of Shuffles',ylabel='R-Value')
    ax.scatter(0,1)
    print("Example output for Run 4: \n" )

    for i in range(15):
        deck = binaryShuffle2(deck)
        rho = find_R_value(deck)
        ax.scatter([i+1],rho)     
        print("Shuffle Number: " + str(i+1) + " | R-Value : " + str(rho))

    fig.subplots_adjust(wspace=.4)    
    plt.show()

    pass

def find_R_value(deck):

    default_deck1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
    default_deck2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                    53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]
    shuffled_deck = deckAsValues(deck)

    if (len(deck) < 100):
        x = default_deck1
    else:
        x = default_deck2

    x = np.vstack((x,shuffled_deck))
    rho = np.corrcoef(x)

    # print(rho)

    return rho[0][1]



def main():
    
    # firstRun()

    # secondRun()

    # thirdRun()

    fourthRun()

    pass



if __name__ == "__main__":
    main()