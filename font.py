import tkinter as tk
from tkinter import font

# Create a Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide the root window if you don't want to show it

# Get a list of available font families
font_families = list(font.families())

# Print the list of font families
for family in font_families:
    print(family)

# You can close the root window if you don't need it
root.destroy()
