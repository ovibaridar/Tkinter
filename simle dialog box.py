from tkinter import *
import tkinter.simpledialog


class my_frame:
    def __init__(self, root):
        self.frame = Frame(root, height=500, width=500, bg="black")
        self.frame.propagate(0)
        self.frame.pack()
        self.buttonn = Button(self.frame, text="Ok", command=self.button)
        self.buttonn.pack()

    def button(self):
        self.name = tkinter.simpledialog.askstring("Input", "what is your name")
        self.age = tkinter.simpledialog.askinteger("Input", "what is your Age")
        print(self.name, self.age)


root = Tk()
root.geometry("500x500")
frame = my_frame(root)

root.mainloop()
