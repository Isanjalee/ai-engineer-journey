import json

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)

print("Name:", data["name"])
print("Role:", data["role"])
print("Skills:", data["skills"])

# Modify data
data["day"] = 3
data["skills"].append("JSON")

# Write back to JSON
with open("data_updated.json", "w") as f:
    json.dump(data, f, indent=2)

print("Updated JSON saved as data_updated.json")
