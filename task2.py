#!python3

"""
##### Task 2 Calculator
Create a simple app that allows you to do a calculation with an arithmetic operation.  You will need a spinbox between 2 entry boxes.  The entryboxes are where you should be entering your numbers, and the spinbox should be the operator.  You will need a button to do the calculation.  You can modify your assignment from A500 for this.
"""

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("500x200")

def calculate():
    a = float(aEntry.get())
    b = float(bEntry.get())
    operator = operatorSpinBox.get()

    if operator == '+':
        outputLabel.configure(text = a + b)
    elif operator == '-':
        outputLabel.configure(text = a - b)
    elif operator == '*':
        outputLabel.configure(text = a * b)
    elif operator == '/':
        outputLabel.configure(text = a // b)

#label
outputLabel = tk.Label(window)

#entries
aEntry = tk.Entry(window)
bEntry = tk.Entry(window)

#spinboxes
operatorSpinBox = ttk.Spinbox(window, values = ['+', '-', '*', '/'], width = 10, justify='center')

#button
enterButton = tk.Button(window, text = "Enter", command = calculate)

#grid
aEntry.grid(row = 1, column = 1)
operatorSpinBox.grid(row = 1, column = 2)
bEntry.grid(row = 1, column = 3)

enterButton.grid(row = 2, column = 2)

outputLabel.grid(row = 3, column = 2, pady = 20)

window.mainloop()