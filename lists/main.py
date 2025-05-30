#Creating the list
fruits= ["apple", "banana", "cherry"]
numbers= [1, 2, 3, 4, 5]
mixed= [1, "apple", 3.14, True]

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[-1]) #cherry


print(fruits[0:2])  # Output: ['apple', 'banana']

#basic operations
fruits.append("orange")  # Adding an element
fruits.insert(1, "kiwi")  # Inserting an element at index 1

fruits.remove("banana")  # Removing an element
last_item=fruits.pop()  # Removing and returning the last element


print("apple" in fruits)  # Checking if an element exists

print(len(fruits))  # Output: 4 (length of the list)

#looping through a list
for fruit in fruits:
    print(fruit)
    
#list methods 
numers= [5,2,9,1,7]

numbers.sort()  # Sorting the list in ascending order
numbers.reverse()  # Reversing the order of the list
numbers.clear()  # Removing all elements from the list

a= [1, 2, 3]
b=a.copy()

#copying a list 
a = [1, 2, 3]
b = a.copy()  # Creates a shallow copy of the list