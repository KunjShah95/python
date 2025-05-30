# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access
print(person["name"])       # Alice

# Update
person["age"] = 26

# Add new key
person["gender"] = "Female"

# Delete
del person["city"]

# Traverse
for key, value in person.items():
    print(f"{key}: {value}")
