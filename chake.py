import customtkinter as ck

# Create a tkinter window
window = ck.CTk()

# Create a table using your customtkinter module
table_data = [
    ["Name", "Age", "City"],
    ["John", 30, "New York"],
    ["Alice", 25, "Los Angeles"],
    ["Bob", 35, "Chicago"]
]

table = ck.CTkTabview(window,width=10)

# Display the table
table.pack()

# Start the tkinter main loop
window.mainloop()
