from tkinter import *

root = Tk()

root.title("My first GUI")
root.geometry("500x500")
root.wm_iconbitmap("img/images.ico")


def gender():
    selected_gender = valu.get()
    if selected_gender == 1:
        leb.config(text="Male")
    elif selected_gender == 2:
        leb.config(text="Female")


frame = Frame(root, width=500, height=500, bg="#926868")
frame.propagate(0)
frame.pack()

valu = IntVar()

rb1 = Checkbutton(frame, text="Male", variable=valu, onvalue=1, offvalue=0)
rb2 = Checkbutton(frame, text="Female", variable=valu, onvalue=2, offvalue=0)
button = Button(frame, text="Ok", command=gender)
leb = Label(frame, bg="#926868")

rb1.pack()
rb2.pack()
button.pack()
leb.pack()

root.mainloop()
