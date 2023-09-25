from tkinter import *

root = Tk()

root.title("My first GUI")
root.geometry("500x500")
root.wm_iconbitmap("img/images.ico")
# root.resizable(False, False)


def click():
    l1 = Label(root, text="After click i am on  ", font=('times new roman', 10, 'bold'), fg="red")
    l1.pack(side=TOP)


button = Button(root, text='Click', font=('arial', 20), command=click)
button.pack()

root.mainloop()
