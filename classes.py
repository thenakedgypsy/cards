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
    
    def getCardDisplay(self):
        if self.getSuit() == "Diamonds":
            return(f"♢ {self.getRank()} of {self.getSuit()} ♢")
        elif self.getSuit() == "Spades":
            return(f"♤ {self.getRank()} of {self.getSuit()} ♤")
        elif self.getSuit() == "Hearts":
            return(f"♡ {self.getRank()} of {self.getSuit()} ♡")
        elif self.getSuit() == "Clubs":
            return(f"♧ {self.getRank()} of {self.getSuit()} ♧")
        else:
            return(f"{self.getRank()} of {self.getSuit()}")
    
    def printCard(self):
        if self.getSuit() == "Diamonds":
            print(f"♢ {self.getRank()} of {self.getSuit()} ♢")
        elif self.getSuit() == "Spades":
            print(f"♤ {self.getRank()} of {self.getSuit()} ♤")
        elif self.getSuit() == "Hearts":
            print(f"♡ {self.getRank()} of {self.getSuit()} ♡")
        elif self.getSuit() == "Clubs":
            print(f"♧ {self.getRank()} of {self.getSuit()} ♧")
        else:
            print(f"{self.getRank()} of {self.getSuit()}")
        


class Deck:
    def __init__(self):
        self.__cardsInDeck = []

    def getDeck(self):
        return self.__cardsInDeck

    def addCard(self,card):
        self.__cardsInDeck.append(card)

    def getCard(self,index):
        return self.__cardsInDeck[index]
    
    def shuffle(self):
        random.shuffle(self.__cardsInDeck)
    
    def discard(self,index):
        del self.__cardsInDeck[index]

    def getDeckSize(self):
        return len(self.__cardsInDeck) -1

    def draw(self):
        if self.getDeckSize() >= 0:
            return self.__cardsInDeck.pop()
            
        else:
            print("Deck is empty.")  
    
    def printDeck(self):
        for card in self.getDeck():
            card.printCard()

    def __iter__(self):
        return iter(self.__cardsInDeck)

class Hand(Deck):
    
    def play(self, playArea, index):
        playArea.addCard(self.getCard(index))
        self.discard(index)


class PlayArea(Deck):
    
    def unPlay(self, hand, index):
        hand.addCard(self.getCard(index))
        self.discard(index)





