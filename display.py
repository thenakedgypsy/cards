import tkinter as tk
from classes import *

class Display:
      
    def __init__(self): #initialises the display object and various instance variables to track hand/playarea etc as well as adding seprators 
        self.root = tk.Tk()
        self.root.title("Cards")
        self.root.geometry("800x400")
        self.handButtons = []
        self.playedButtons = []
        self.handFirstPack = True
        self.playFirstPack = True
        self.separator = tk.Label(self.root, text="----------------------------------------PLAYED CARDS----------------------------------------")
        self.separator2 = tk.Label(self.root, text="-------------------------------------------HAND-------------------------------------------")
 
    def updatePlayArea(self, playArea, hand): #updates the play area and seperators displays
        self.separator.grid(row=0, column=0, columnspan=50, pady=5)
        if self.playFirstPack == False:
            for button in self.playedButtons:
                button.grid_forget()
            self.playedButtons.clear()
        i = 1
        for i, card in enumerate(playArea, start = 0):
            btn = tk.Button(self.root, text=card.getCardDisplay(),height=6, padx=5, pady=5, command=lambda i=i: self.playCardClicked(playArea,hand,i)) # this lambda function captures i at the moment the button is...
            btn.grid(row=1, column=i, padx=5)                                                      #...created, rather than at the end. 
            self.playedButtons.append(btn)
            i += 1
        self.playFirstPack = False

        self.separator2.grid(row=2, column=0, columnspan=50, pady=5)

    def updateHand(self,hand,playArea): #updates the hand display
        if self.handFirstPack == False:
            for button in self.handButtons:
                button.grid_forget()
            self.handButtons.clear()
        for i, card in enumerate(hand, start = 0 ):
            btn = tk.Button(self.root, text=card.getCardDisplay(), height=6, padx=5, pady=5, command=lambda i=i: self.handCardClicked(hand,playArea,i)) # this lambda function captures i at the moment the button is...
            btn.grid(row=3, column=i, padx=5)
            self.handButtons.append(btn)
        self.handFirstPack = False

    def handCardClicked(self,hand,playArea,index): #moves the clicked card from the hand to the play area
        hand.play(playArea,index)
        self.updateDisplay(hand,playArea)

    def playCardClicked(self,playArea,hand,index): #moves the clicked card from the play area to the hand
        playArea.unPlay(hand,index)
        self.updateDisplay(hand,playArea)

    def labelMaster(self): # placeholder
        pass

    def updateDisplay(self, hand, playArea): #updates the entire display
        self.updatePlayArea(playArea,hand)

        self.updateHand(hand,playArea)

    def beginDisplay(self): #begins the tkinter loop
        
        self.root.mainloop()
