from tkinter import *
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from tkinter import messagebox

import webbrowser
root = Tk()

# Design part
root.title("Chat Bot")
root.geometry("500x500")
root.wm_iconbitmap("img/download.ico")
root.resizable(False, False)
heading = Label(root, text="Chat Bot", font=('arial', 15, "bold"))
heading.pack()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# Create a frame to contain the Listbox and scrollbar
list_frame = Frame(root)
list_frame.pack(fill=BOTH, expand=True)

# Set the number of visible rows in the Listbox to 5
listbox_height = 5

mylist = Listbox(list_frame, yscrollcommand=scrollbar.set, height=listbox_height, width=400)
mylist.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=mylist.yview)


def user():
    user_chat = input_text.get()
    if user_chat.strip():
        mylist.insert(END, "User: " + user_chat)
        mylist.see(END)  # Scroll down to the last item
        input_entry.delete(0, END)
        bot_response = get_bot_response(user_chat)
        mylist.insert(END, "Bot: " + bot_response)
        mylist.see(END)  # Scroll down to the last item
    else:
        messagebox.showinfo("Warning", "Please fill in the entry!")


def get_bot_response(user_input):
    user_input = user_input.lower()  # Convert to lowercase for case-insensitive matching
    dictionary = [
        ("afaf", "Sorry, I didn't understand your question."),
        ("hi", "Hi, I am a chatbot. You?"),
        ("your name?", "I am a chatbot. You?"),
        ("my name is ", "Oh, nice name."),
        ("i am", "Oh, nice name."),
        ("how are you?", "I am fine. How can I assist you?"),
        ("can you help me", "Yes, how can I help you?"),
        ("i am fine", "That's great to hear! How can I help you today?"),
        ("how old are you?", "I am just a computer program, so I don't have an age."),
        ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!"),
        ("can you sing a song", "songw"),
        ("nice", "Thank you")
    ]

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(dictionary, columns=["Que", "Ans"])

    # Initialize the TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit and transform the questions in the dictionary
    tfidf_matrix = vectorizer.fit_transform(df["Que"])

    # Transform the user's input
    user_tfidf = vectorizer.transform([user_input])

    # Calculate cosine similarities between user input and dictionary questions
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix)

    # Find the index of the most similar question
    most_similar_index = cosine_similarities.argmax()

    # Get the corresponding answer
    response = df.iloc[most_similar_index]["Ans"]

    if response == "songw":
        youtube_url = "https://www.youtube.com/watch?v=aVR0-gSoHa8&ab_channel=DebdulalAditya"
        webbrowser.open(youtube_url)
        return "How is it ?"
    elif response:
        return response



input_text = StringVar()
input_entry = Entry(root, textvariable=input_text, font=('arial', 15), width=35)
input_entry.pack(padx=10, pady=10)

button = Button(root, text="Send", font=('arial', 10), bg="black", fg="white", command=user)
button.pack(padx=10, pady=10)

root.bind("<Return>", lambda event=None: user())

root.mainloop()
