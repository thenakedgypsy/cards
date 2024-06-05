import tkinter as tk
import random

def main():
    print("Booting...")
    render()

def render(): #renders a box with two buttons
    root = tk.Tk()
    root.title("WHAT IS THIS?")

    label= tk.Label(root, text="THIS IS A WINDOW")
    label.pack()

    button = tk.Button(root, text="Press", command=lambda: label.config(text="Alice <3"))
    button.pack()
    button2 = tk.Button(root, text="Dont Press", command=lambda: label.config(text="Alice is a poo"))
    button2.pack()
    root.mainloop()


main()


