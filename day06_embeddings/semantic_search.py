from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load documents
with open("data.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Convert text to vectors
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

# User query
query = input("Ask a question: ")

query_vector = vectorizer.transform([query])

# Compute similarity
scores = cosine_similarity(query_vector, doc_vectors)[0]

# Get best match
best_index = scores.argmax()

print("\nBest semantic match:")
print(documents[best_index])
