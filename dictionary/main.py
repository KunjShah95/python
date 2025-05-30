#creating a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Or using dict() constructor:
person2 = dict(name="Bob", age=30, city="London")

# Accessing values
print(person["name"])    # Alice

# Using get() method (safer if key may not exist)
print(person.get("age")) # 25
print(person.get("job", "Not specified"))  # Returns default if key not found


#adding and updating values
person["job"] = "Engineer"  # Adds new key-value pair
person["age"] = 26          # Updates existing key

#removing items
person.pop("city")      # Removes key 'city'
person.popitem()        # Removes last inserted item (Python 3.7+)
del person["age"]       # Deletes key 'age'
person.clear()          # Clears the dictionary


#looping through a dictionary
for key in person:
    print(key, ":", person[key])

# Or more explicitly
for key, value in person.items():
    print(f"{key} -> {value}")
