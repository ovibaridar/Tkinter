from tkinter import *

root = Tk()

root.title("My first GUI")
root.geometry("500x500")
root.wm_iconbitmap("img/images.ico")
# root.resizable(False, False)
l1 = Label(text="Grid1", font=('times new roman', 10, 'bold'), fg="red")
l1.grid(row=0, column=0)


l2 = Label(text="Grid2", font=('times new roman', 10, 'bold'), fg="red")
l2.grid(row=0, column=1)

l3 = Label(text="Grid3", font=('times new roman', 10, 'bold'), fg="red")
l3.grid(row=1, column=0)

l4 = Label(text="Grid4", font=('times new roman', 10, 'bold'), fg="red")
l4.grid(row=1, column=1)


root.mainloop()

