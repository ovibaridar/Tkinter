from tkinter import *
import customtkinter as ctk

root = Tk()
root.title("frame ")
root.geometry("500x500")

frame =Frame(root, height=500, width=500, bg="#926868")
frame.propagate(0)
frame.pack()

frame2 = ctk.CTkScrollableFrame(frame, height=200, width=300)
frame2.pack(pady=20)

b = ctk.CTkButton(frame2, text="ok", width=5, height=2)
b.pack(fill="x")

root.mainloop()
