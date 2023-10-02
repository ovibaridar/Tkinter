from tkinter import *


def color(n):
     frame["bg"] = n


root = Tk()
root.title("NON")
root.geometry("700x700")
frame = Frame(root, width=700, height=700, bg="black")
frame.propagate(0)
frame.pack()

button1 = Button(frame, text="red", width=50, height=10, command=lambda: color("red"))
button1.pack()
button2 = Button(frame, text="Brown", width=50, height=10, command=lambda: color("#926868"))
button2.pack()

root.mainloop()
