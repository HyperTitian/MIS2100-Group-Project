import tkinter as tk
import os

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=700)
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.6, relx=0.1, rely=0.1)

nameLabel = tk.Label(root, text="Enter your name:")
nameLabel.pack()

textField = tk.Entry(root)
textField.pack()

def myClick():
    testLabel = tk.Label(frame,  text="Congrats " + textField.get() + "! You clicked the button!", bg="white")
    testLabel.pack()

testButton = tk.Button(root, text="Click this button!", padx=10, pady=5, fg="white", bg="black", command=myClick)
testButton.pack()



root.mainloop()
