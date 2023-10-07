import customtkinter as ck

root = ck.CTk()
root.title("Entry your name")
root.geometry("600x400")
root.resizable(False, False)

frame = ck.CTkFrame(root, border_width=1)
frame.grid(pady=(120), padx=(10, 10), row=0, column=0)

entry1 = ck.CTkEntry(frame, placeholder_text="First name")
entry1.grid(pady=(10, 10), padx=(10, 10), row=0, column=0)
entry2 = ck.CTkEntry(frame, placeholder_text="Second name")
entry2.grid(pady=(10, 10), padx=(10, 10), row=1, column=0)
entry3 = ck.CTkEntry(frame, placeholder_text="Email")
entry3.grid(pady=(10, 10), padx=(10, 10), row=2, column=0)
button = ck.CTkButton(frame, text="Done")
button.grid(row=3, column=0, pady=(0, 10))

root.mainloop()
