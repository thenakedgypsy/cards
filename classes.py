import random

class Card:
    def __init__(self, suit, rank): #initialise a card with a suit and rank
        self.__suit = suit
        self.__rank = rank

    def setSuit(self, suit): # sets the card suit
        self.__suit = suit
        
    def getSuit(self): #returns the card suit
        return self.__suit
    
    def setRank(self, rank): #sets the card rank
        self.__rank = rank

    def getRank(self): #returns the card rank
        return self.__rank
    
    def getCardDisplay(self): #returns a string representation of the card
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
    
    def printCard(self): #prints a card
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
    def __init__(self):#initialises object witrh a list
        self.__cardsInDeck = []

    def getDeck(self): #returns the list of cards 
        return self.__cardsInDeck

    def addCard(self,card): #adds a card to the deck
        self.__cardsInDeck.append(card)

    def getCard(self,index): #returns a card at index
        return self.__cardsInDeck[index]
    
    def shuffle(self): #shuffles the deck
        random.shuffle(self.__cardsInDeck)
    
    def discard(self,index): #removes a card from the deck at index
        del self.__cardsInDeck[index]

    def getDeckSize(self): #returns the number of cards in the deck
        return len(self.__cardsInDeck) -1

    def draw(self): #returns the top card of the deck or prints an error
        if self.getDeckSize() >= 0:
            return self.__cardsInDeck.pop()
            
        else:
            print("Deck is empty.")  
    
    def printDeck(self): #prints each card in the deck
        for card in self.getDeck():
            card.printCard()

    def __iter__(self): #makes the deck iterable
        return iter(self.__cardsInDeck)

class Hand(Deck): 
    
    def play(self, playArea, index): #removes a card from the hand and adds it to the playArea
        playArea.addCard(self.getCard(index))
        self.discard(index)


class PlayArea(Deck): 
    
    def unPlay(self, hand, index): #removes a card from the playArea and returns it to the hand 
        hand.addCard(self.getCard(index))
        self.discard(index)





