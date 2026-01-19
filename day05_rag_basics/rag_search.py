def search(query, data):
    results = []
    for line in data:
        if query.lower() in line.lower():
            results.append(line.strip())
    return results


# Load knowledge base
with open("data.txt", "r") as file:
    lines = file.readlines()

user_query = input("Ask a question: ")

matches = search(user_query, lines)

if matches:
    print("\nRelevant information found:")
    for m in matches:
        print("-", m)
else:
    print("\nNo relevant information found.")
