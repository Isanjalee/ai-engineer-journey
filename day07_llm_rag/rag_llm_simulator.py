from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load knowledge base
with open("knowledge.txt", "r") as f:
    documents = [line.strip() for line in f.readlines()]

# Vectorize documents
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def retrieve_context(query):
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, doc_vectors)[0]
    best_index = scores.argmax()
    return documents[best_index]

def llm_simulator(context, question):
    return f"Question: {question}\n Based on my knowledge: {context}"


# Chat loop
print("AI Assistant (type 'exit' to quit)\n")

while True:
    user_question = input("You: ")
    if user_question.lower() == "exit":
        break

    context = retrieve_context(user_question)
    answer = llm_simulator(context, user_question)

    print("AI:", answer)
