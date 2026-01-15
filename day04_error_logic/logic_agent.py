def decide_action(text):
    if "error" in text.lower():
        return "LOG"
    elif "buy" in text.lower():
        return "NOTIFY"
    else:
        return "IGNORE"

messages = [
    "System error detected",
    "User wants to buy product",
    "Just saying hi"
]

for msg in messages:
    action = decide_action(msg)
    print(f"Message: {msg}")
    print("Action:", action)
    print("----")
