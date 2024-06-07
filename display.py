import tkinter as tk

class Display:
      
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Title")
        self.root.geometry("600x400")
        self.handButtons = []
        self.playedButtons = []
 
    def updatePlayArea(self, playarea):
        self.playedButtons.pack_forget()
        i = 1
        for card in hand:
            btn = tk.Button(self.root, card.getCardDisplay(), command=lambda i=i: self.handCardClicked(playarea,i)) # this lambda function captures i at the moment the button is...
            btn.pack(padx=5)                                                      #...created, rather than at the end. 
            self.playedButtons.append(btn)
            i += 1

    def updateHand(self,hand):
        self.handButtons.pack_forget()
        i = 1
        for card in hand:
            btn = tk.Button(self.root, card.getCardDisplay(), command=lambda i=i: self.handCardClicked(hand,i)) # this lambda function captures i at the moment the button is...
            btn.pack(padx=5)                                                      #...created, rather than at the end. 
            self.handButtons.append(btn)
            i += 1

    def handCardClicked(self,hand,index):
        pass

    def labelMaster(self):
        pass

    def beginDisplay(self):
        self.root.mainloop()
