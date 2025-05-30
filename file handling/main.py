import os

# 🔹 1. Writing to a new file (overwrites if exists)
with open("demo.txt", "w") as file:
    file.write("Line 1: Hello, this is a demo file.\n")
    file.write("Line 2: File handling in Python is easy.\n")

# 🔹 2. Reading the entire content
with open("demo.txt", "r") as file:
    content = file.read()
    print("🔸 Reading entire file:")
    print(content)

# 🔹 3. Appending to the existing file
with open("demo.txt", "a") as file:
    file.write("Line 3: This line is appended.\n")

# 🔹 4. Reading line by line
with open("demo.txt", "r") as file:
    print("\n🔸 Reading line by line:")
    for line in file:
        print(line.strip())

# 🔹 5. File existence check before reading
filename = "demo.txt"
if os.path.exists(filename):
    with open(filename, "r") as file:
        print("\n🔸 File exists. Showing last line only:")
        lines = file.readlines()
        print(lines[-1].strip())
else:
    print("File does not exist!")

# 🔹 6. Trying to open a non-existent file in 'x' mode (fails if file exists)
try:
    with open("demo.txt", "x") as file:
        file.write("Trying to create a new file.")
except FileExistsError:
    print("\n🔸 File already exists. Cannot create with 'x' mode.")
