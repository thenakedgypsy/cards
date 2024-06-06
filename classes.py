import random

class Card:
    def __init__(self, suit, rank):
        self.__suit = suit
        self.__rank = rank

    def setSuit(self, suit):
        self.__suit = suit
        
    def getSuit(self):
        return self.__suit
    
    def setRank(self, rank):
        self.__rank = rank

    def getRank(self):
        return self.__rank
    
    def printCard(self):
        print(f"{self.getRank()} of {self.getSuit()}s")


class Deck:
    def __init__(self):
        self.__cardsInDeck = []

    def addCard(self,card):
        self.__cardsInDeck.append(card)

    def getCard(self,index):
        return self.__cardsInDeck[index]
    
    def shuffle(self):
        random.shuffle(self.__cardsInDeck)
    
    def discard(self,index):
        del self.__cardsInDeck[index]

    def draw(self):
        return self.__cardsInDeck.pop()
    
    def printDeck(self):
        print(self.__cardsInDeck)



