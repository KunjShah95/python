#Creating a set
# A set is an unordered collection of unique elements.
# Sets are useful for membership testing and eliminating duplicate entries.

# Creating a set
numbers={1, 2, 3, 4, 5}
duplicates={1, 2, 2, 3}  # Duplicates are automatically removed
print(duplicates)

#using the set constructor

s= set([1, 2, 3, 4, 5])

#Adding and removing elements
s= {1, 2, 3}
s.add(4)  # Adding an element
s.remove(2)  # Removing an element
s.discard(10)  # Discarding an element (no error if not found)
s.clear()  # Removing all elements

a = {1, 2, 3}
b = {3, 4, 5}

# Set operations
print(a | b)   # Union → {1, 2, 3, 4, 5}
print(a & b)   # Intersection → {3}
print(a - b)   # Difference → {1, 2}
print(a ^ b)   # Symmetric Difference → {1, 2, 4, 5}


#looping through a set
for item in {"apple", "banana", "cherry"}:
    print(item)


"""✅ When to Use Sets:
To remove duplicates from a list

When order doesn’t matter

For set math (union, intersection, etc.)
"""