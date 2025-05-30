#Creating a tuple
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "apple", 3.14, True)

one_item= (42,)  # Single item tuple (note the comma)


# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry 
print(fruits[0:2])  # Output: ('apple', 'banana')

#tupples are immutable, so we cannot modify them
fruits = ("apple", "banana", "cherry")
# fruits[0] = "orange"  ❌ This will raise an error


#only two common operations
t = (1, 2, 2, 3, 4)

print(t.count(2))   # Output: 2
print(t.index(3))   # Output: 3 (index of first occurrence)

#tupple unpacking
person = ("John", 30, "Engineer")
name,age,job= person  # Unpacking the tuple
print(name)  # Output: John