#len()
print(len("Hello, World!"))  # Output: 13

print(len([1, 2, 3, 4, 5]))  # Output: 5

#type()
print(type(10))            # <class 'int'>
print(type([1, 2, 3]))    # <class 'list'>

#int(), float(), str()
print(int("123"))         # Output: 123
print(float("3.14"))      # Output: 3.14
print(str(456))           # Output: '456'

#input()
name = input("Enter your name: ")
print(f"Hello, {name}!")


#sum()
print(sum([1, 2, 3, 4]))  # 10

#max(), min()
print(max([1, 2, 3, 4]))  # Output: 4
print(min([1, 2, 3, 4]))  # Output: 1

#range()
for i in range(5):
    print(i)
    
#ennumerate()
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)

#zip()
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(name, age)
