from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample texts
text1 = "How are you?"
text2 = "how you"

# Convert the texts into TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform([text1, text2])

# Calculate the cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

# Similarity score ranges from 0 to 1, where 1 means identical
if cosine_sim[0][0] == 1.0:
    print("The texts are identical.")
elif cosine_sim[0][0] > 0.7:
    print("The texts are very similar.")
else:
    print("The texts are not similar.")
