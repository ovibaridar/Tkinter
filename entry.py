from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("My first GUI")
root.geometry("500x500")
root.wm_iconbitmap("img/images.ico")
# root.resizable(False, False)

entry = Entry(root, width=50, font=('times new roman', 10, 'bold'))
entry.pack(pady=10)


def click():
    user_input = entry.get()
    if user_input != "":
        l1 = Label(root, text=user_input, font=('times new roman', 10, 'bold'), fg="red")
        l1.pack(side=TOP)
        entry.delete(0, END)  # Clear the Entry widget
    else:
        messagebox.showinfo("Warning", "Please fill in the entry!")


button = Button(root, text='Click', font=('arial', 20), command=click)
button.pack(pady=20)

root.bind("<Return>", lambda event=None: click())  # button work when hit  enter

root.mainloop()
