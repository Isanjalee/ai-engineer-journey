# io_demo.py
filename = "output.txt"

# Step 1: Take input
user_input = input("Enter a message: ")

# Step 2: Write to file
with open(filename, "w") as file:
    file.write(user_input)

# Step 3: Read and print
with open(filename, "r") as file:
    content = file.read()
    print("You wrote:", content)
