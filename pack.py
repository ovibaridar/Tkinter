from tkinter import *

root = Tk()

root.title("My first GUI")
root.geometry("500x500")
root.wm_iconbitmap("img/images.ico")
# root.resizable(False, False)

l1 = Label(root, text="Top", font=('times new roman', 10, 'bold'), fg="red")
l1.pack(side=TOP)

l1 = Label(root, text="LEFT", font=('times new roman', 10, 'bold'), fg="green")
l1.pack(side=LEFT)

l1 = Label(root, text="RIGHT", font=('times new roman', 10, 'bold'), fg="green")
l1.pack(side=RIGHT)

l1 = Label(root, text="BOTTOM", font=('times new roman', 10, 'bold'), fg="red")
l1.pack(side=BOTTOM)

root.mainloop()
