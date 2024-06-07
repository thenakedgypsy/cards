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

    print("Printing Deck:")
    mainDeck.printDeck()
    print("--------------------")
    print("Shuffling...")
    mainDeck.shuffle()
    print("Drawing:")
    mainDeck.draw()
    print("Drawing:")
    mainDeck.draw()
    print("Drawing:")
    mainDeck.draw()
    display = Display()
    display.beginDisplay()


main()
