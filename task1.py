"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""

import tkinter as tk
from tkinter import ttk
import calendar

window = tk.Tk()
window.geometry("500x200")

def enter():
    day = dayCombo.get()
    month = monthCombo.get()
    year = yearCombo.get()

    outputLabel.configure(text = f"You were born on\n{day} {month}, {year}")

#labels
dayLabel = tk.Label(window, text = "Day")
monthLabel = tk.Label(window, text = "Month")
yearLabel = tk.Label(window, text = "Year")

outputLabel = tk.Label(window)

#comboboxes
dayCombo = ttk.Combobox(window, values = list(range(1, 32)))
monthCombo = ttk.Combobox(window, values = list(calendar.month_name[1:]))
yearCombo = ttk.Combobox(window, values = list(range(1900, 2024)))

#button
enterButton = tk.Button(window, text = "Enter", command = enter)

dayLabel.grid(row = 1, column = 1)
monthLabel.grid(row = 1, column = 2)
yearLabel.grid(row = 1, column = 3)

dayCombo.grid(row = 2, column = 1)
monthCombo.grid(row = 2, column = 2)
yearCombo.grid(row = 2, column = 3)

enterButton.grid(row = 3, column = 2)

outputLabel.grid(row = 4, column = 2, pady = 20)

window.mainloop()