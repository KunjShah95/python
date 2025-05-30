#Syntax
# new_list = [expression for item in iterable if condition ]


#Squares of numbers 1 to 5 with simple example
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

#with conditions
evens= [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)

#using strings

#extracting vowels from a string

sentence = "Hello, World!"
vowels = [char for char in sentence if char.lower() in "aeiou"]
print("Vowels:", vowels)


#Nested loops in list comprehension

#create pairs (x,y) from two lists
pairs = [(x,y) for x in range(1, 4) for y in ['a', 'b']]
print("Pairs:", pairs)