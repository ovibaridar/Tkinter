from tkinter import *
from tkinter import ttk
from random import choice

root = Tk()
root.title("Table")

Name = ["Al Arman ovi", "koli Akter", "Nahid Hasan", "Nayeem Islam", "Abdulla Al Muksit", "Abdur rashid raskin",
        "Farhana Runu", "Tania Akter", "Toufic Ahamed"]
Roll = ["1013", "1010", "1007", "1011", "1008", "1012", "1003", "1006", "1001"]
Department = ["Cse", "Cse", "Cse", "Cse", "Cse", "Cse", "Cse", "Cse", "Cse"]

table = ttk.Treeview(root, columns=("Name", "Roll", "Department"), show="headings")
table.heading("Name", text="Name")
table.heading("Roll", text="Roll")
table.heading("Department", text="Department")
table.pack(fill="both", expand=True)

for i in range(0, len(Roll)):
    name = Name[i]
    roll = Roll[i]
    dep = Department[i]
    data = (name, roll, dep)
    table.insert(parent="", index=0, values=data)


# def select(_):
#     for i in table.selection():
#         print(table.item(i)["values"])


def delete(_):
    for i in table.selection():
        table.delete(i)


# table.bind("<<TreeviewSelect>>", select)
table.bind("<Delete>", delete)

root.mainloop()
