import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)

# Initialize a variable to track the current theme
current_theme = "forest-dark"


def toggle():
    global current_theme
    if current_theme == "forest-dark":
        if "forest-light" not in style.theme_names():
            root.tk.call('source', 'forest-light.tcl')
        style.theme_use('forest-light')
        current_theme = "forest-light"
    else:
        style.theme_use('forest-dark')
        current_theme = "forest-dark"


style = ttk.Style(root)
if "forest-dark" not in style.theme_names():
    root.tk.call('source', 'forest-dark.tcl')
style.theme_use('forest-dark')

frame1 = ttk.Frame(root, height=400, width=600)
frame1.pack()
mode = ttk.Checkbutton(frame1, style="Switch", command=toggle)
mode.place(x=550, y=10)

# Create a Frame with just a border
frame2 = ttk.Frame(frame1, height=200, width=200, relief="groove", borderwidth=2)
frame2.place(x=30, y=80)

font = ("Times New Roman CE", 10)

entry0 = ttk.Entry(frame2, font=font)
entry0.insert(0, "Enter your first name")
entry0.bind("<FocusIn>", lambda e: entry0.delete(0, "end"))
entry0.pack(pady=(10, 10), padx=(10, 10))

entry1 = ttk.Entry(frame2, font=font)
entry1.insert(0, "Enter your last name")
entry1.bind("<FocusIn>", lambda e: entry1.delete(0, "end"))
entry1.pack(pady=(10, 10), padx=(10, 10))

entry2 = ttk.Entry(frame2, font=font)
entry2.insert(0, "Enter your Email")
entry2.bind("<FocusIn>", lambda e: entry2.delete(0, "end"))
entry2.pack(pady=(10, 10), padx=(10, 10))

entry3 = ttk.Entry(frame2, font=font)
entry3.insert(0, "Enter your Address")
entry3.bind("<FocusIn>", lambda e: entry3.delete(0, "end"))
entry3.pack(pady=(10, 10), padx=(10, 10))

entry4 = ttk.Button(frame2, text="ok")
entry4.pack(pady=(10, 10), padx=(10, 10))

root.mainloop()
