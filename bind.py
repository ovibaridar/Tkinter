from tkinter import *

root = Tk()
font = ("Arial", 15, "bold")


def entryget(event):
    value = entry.get()
    le1.config(text=value)


root.title("Bind check")
root.geometry("500x500")

frame1 = Frame(root, height=500, width=500, bg="#926868")
frame1.propagate(0)
frame1.pack()

entry = Entry(frame1, width=30, font=font)
entry.pack()

le1 = Label(frame1, font=font, bg="#926868")
le1.pack()

entry.bind('<Return>', entryget)

root.mainloop()
