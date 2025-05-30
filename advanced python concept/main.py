#  map(), filter(), reduce(), zip()
from functools import reduce

nums=[1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # Output: [1, 4, 9, 16, 25]


evens= list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4]

total= reduce(lambda x, y: x + y, nums)
print(total)  # Output: 15

names= ["Alice", "Bob", "Charlie"]
ages= [25, 30, 35]
combined = list(zip(names, ages))
print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# Comprehensions (List, Set, Dict)

#list comprehension
squared_list = [x**2 for x in nums]
print(squared_list)  # Output: [1, 4, 9, 16, 25]

# set comprehension
unique= {x**2 for x in [1, 2, 2, 3, 4]}
print(unique)  # Output: {1, 4, 9, 16}

# dict comprehension
squared_dict = {x: x**2 for x in nums}
print(squared_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
