from classes import *
from display import *
import tkinter

def makeStandardDeck(deck):   # could be a class? DeckBuilder?
    print("Making a deck...")
    deck = deck
    suitList = ["Spades","Hearts","Diamonds","Clubs"]
    rankList = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    for suit in suitList:
        for rank in rankList:
            card = Card(suit,rank)
            deck.addCard(card)





def main():
    print("Program Launching...")
    
    mainDeck = Deck()
    makeStandardDeck(mainDeck)
    aHand = Hand()
    playArea = PlayArea()


    print("Printing Deck:")
    mainDeck.printDeck()
    print("--------------------")
    print("Shuffling...")
    mainDeck.shuffle()
    print("Drawing:")
    aHand.addCard(mainDeck.draw())
    aHand.printDeck()
    print("Drawing:")
    aHand.addCard(mainDeck.draw())
    aHand.printDeck()
    print("Drawing:")
    aHand.addCard(mainDeck.draw())
    aHand.printDeck()
    print("Drawing:")
    aHand.addCard(mainDeck.draw())
    aHand.printDeck()
    print("Drawing:")
    aHand.addCard(mainDeck.draw())
    aHand.printDeck()
    print("Printing Hand:")
    aHand.printDeck()

    display = Display()
    print("sending buttons to hand")
    display.updateDisplay(aHand, playArea)
    display.beginDisplay()

    



main()
