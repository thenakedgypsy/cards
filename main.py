import tkinter as tk
import random

def main():
    # creating the window with a pad
    root = tk.Tk()
    root.title("Two Buttons")
    pad = tk.Label(root, text="----------------------------------------------------------------")
    pad.pack(pady=10)

    # some variables that can be updated later
    buttonText = "+ 1"
    button2Text = " - 1 "
    mainTextString = ""
    buttonBool = False
    button2Bool = False
    value = 0

    #update labels based on presses
    def update():
        nonlocal buttonText, mainText, buttonBool, button2Bool, value
   
        # If button 1 pressed
        if buttonBool:
            value += 1
            mainTextString = f"{value}"
            buttonBool = False
       
        # When button 2 pressed
        if button2Bool:
            value -=1
            mainTextString = f"{value}"
            button2Bool = False
        
        # Update labels and button texts
        mainText.config(text = mainTextString)
        button.config(text = buttonText)
        button2.config(text = button2Text)
    
    def buttonPressed(): #sets a bool if button is pressed
        nonlocal buttonBool
        buttonBool = True
        update()

    def button2Pressed(): #sets a bool if button2 is pressed
        nonlocal button2Bool
        button2Bool = True
        update()

    #create main label
    mainText = tk.Label(root, text="0")
    mainText.pack(pady=10)

    # create buttons linked to functions
    button = tk.Button(root, text=buttonText, command=buttonPressed)
    button.pack(pady=2)

    button2 = tk.Button(root, text=button2Text, command=button2Pressed)
    button2.pack(pady=10)

    # create bottom pad
    lowPad = tk.Label(root, text="----------------------------------------------------------------")
    lowPad.pack(pady=10)

    # run tkinters mainloop
    root.mainloop()

main()
