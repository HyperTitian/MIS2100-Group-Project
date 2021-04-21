# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# The important stuff
from tkinter import *
root = Tk()
root.geometry("600x600")

# Import pictures
bg = PhotoImage(file = "C:/Users/hands/MIS2100 Group Project/Background.png", master = root)
string = PhotoImage(file = "C:/Users/hands/MIS2100 Group Project/String.png", master = root)
text = PhotoImage(file = "C:/Users/hands/MIS2100 Group Project/Text.png", master = root)
button = PhotoImage(file = "C:/Users/hands/MIS2100 Group Project/Button.png", master = root)

# Frame the GUI
canvas = Canvas(root, width = 400, height = 400, highlightthickness = 0)
canvas.pack(fill = "both", expand = True)
canvas.create_image(0, 0, image = bg, anchor = "nw")

string1 = Label(root, width = 200, height = 20, image = string, highlightthickness = 2)
string1.place(x = 50, y = 70)

string2 = Label(root, width = 200, height = 20, image = string, highlightthickness = 2)
string2.place(x = 50, y = 130)

string3 = Label(root, width = 200, height = 20, image = string, highlightthickness = 2)
string3.place(x = 340, y = 70)

string4 = Label(root, width = 200, height = 20, image = string, highlightthickness = 2)
string4.place(x = 340, y = 130)

string5 = Label(root, width = 200, height = 20, image = string, highlightthickness = 2)
string5.place(x = 340, y = 190)

text1 = Label(root, width = 200, height = 200, image = text, highlightthickness = 2)
text1.place(x = 50, y = 240)

text2 = Label(root, width = 200, height = 200, image = text, highlightthickness = 2)
text2.place(x = 340, y = 240)

# Things that move
button1 = Button(root, width = 50, height = 50, image = button)
button1.place(x = 50, y = 460)

button2 = Button(root, width = 50, height = 50, image = button)
button2.place(x = 340, y = 460)

output1 = Text(root, width = 19, height = 10, bg = "#071A33", fg = "white", wrap = WORD, borderwidth = 0)
output1.place(x = 72, y = 276)
output1.insert(END, "This is output field 1")

output2 = Text(root, width = 19, height = 10, bg = "#071A33", fg = "white", wrap = WORD, borderwidth = 0)
output2.place(x = 362, y = 276)
output2.insert(END, "This is output field 2")

input1 = Entry(root, width = 33, bg = "#0E294A", fg = "white")
input1.place(x = 54, y = 74)

input2 = Entry(root, width = 33, bg = "#0E294A", fg = "white")
input2.place(x = 54, y = 134)

input3 = Entry(root, width = 33, bg = "#0E294A", fg = "white")
input3.place(x = 344, y = 74)

input4 = Entry(root, width = 33, bg = "#0E294A", fg = "white")
input4.place(x = 344, y = 134)

input5 = Entry(root, width = 33, bg = "#0E294A", fg = "white")
input5.place(x = 344, y = 194)

# The really important stuff
root.mainloop()