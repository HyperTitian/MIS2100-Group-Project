# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tkr
from tkinter import Button
from tkinter import PhotoImage

tk = tkr.Tk()

canvas = tkr.Canvas(tk, width = 250, height = 250)
canvas.grid()

button = Button(tk, text = "I'm a button")
button.place(x = 100, y = 100)

button1 = Button(tk, text = "I'm another button")
button1.place(x = 100, y = 150)

orangeButton = Button(tk, highlightthickness = 0, bd = 0)
png = tkr.PhotoImage(file = "C:/Users/hands/MIS2100 Group Project/OrangeButton.png", master = tk)
orangeButton.config(image = png)
orangeButton.place(x = 100, y = 200)

tk.mainloop()
