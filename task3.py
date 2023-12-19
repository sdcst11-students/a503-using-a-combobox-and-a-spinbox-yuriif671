#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x200")

def calculate():
    p = float(pEntry.get())
    r = float(rEntry.get())
    n = float(nEntry.get())
    t = float(tEntry.get())
    #'P(1+r/n)^(n*t)'
    outputLabel.configure(text = f"A = {round(p * (1 + (r / 100) / n)**(n * t), 2)}$")

#label
pLabel = tk.Label(window, text = "Principal")
rLabel = tk.Label(window, text = "Interest rate")
nLabel = tk.Label(window, text = "Compound periods")
tLabel = tk.Label(window, text = "Years")

outputLabel = tk.Label(window)

#entries
pEntry = tk.Entry(window)
rEntry = tk.Entry(window)
nEntry = tk.Entry(window)
tEntry = tk.Entry(window)

#button
enterButton = tk.Button(window, text = "Enter", command = calculate)

#grid
pLabel.grid(row = 1, column = 1)
rLabel.grid(row = 1, column = 2)
nLabel.grid(row = 1, column = 3)
tLabel.grid(row = 1, column = 4)

pEntry.grid(row = 2, column = 1)
rEntry.grid(row = 2, column = 2)
nEntry.grid(row = 2, column = 3)
tEntry.grid(row = 2, column = 4)

enterButton.grid(row = 3, column = 2)

outputLabel.grid(row = 4, column = 2, pady = 20)

window.mainloop()