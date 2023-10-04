from tkinter import *


class chake_ag:
    def __init__(self, frame):
        self.lb1 = Label(frame, text="This is the text")
        self.lb1.pack()


class chake:
    def __init__(self, root):
        self.frame = Frame(root, height=500, width=500, bg="green")
        self.frame.propagate(0)
        self.frame.pack()
        self.leb = chake_ag(self.frame)


root = Tk()
root.title("Tk")
root.geometry("500x500")
m1 = chake(root)

root.mainloop()
