import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

while (True):
    # Define the user's input
    user_input = input("User: ")

    # Define the dictionary of questions and answers
    dictionary = [
        ("hi", "Hi, I am a chatbot. You?"),
        ("My name is ", "Oh nice name ."),
        ("how are you?", "I am fine. How can I assist you?"),
        ("can you help me", "Yes , How can i help you ?"),
        ("i am fine", "That's great to hear! How can I help you today?"),
        ("how old are you?", "I am just a computer program, so I don't have an age."),
        ("tell me a joke", "Why don't scientists trust atoms? Because they make up everything!")
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

    # Print the response
    print("Chatbot:", response)
