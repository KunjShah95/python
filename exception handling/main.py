"""
Python uses exceptions to handle errors during program execution, so the program doesn’t crash unexpectedly.

 Why Use Exceptions?
Catch and handle errors gracefully

Prevent program from crashing

Debug and log issues effectively

"""

try:
    x=int(input("Enter a number: "))
    result = 10 / x
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")
    
try:
    nums = [1, 2, 3]
    print(nums[5])
except IndexError:
    print("Index out of range!")


try:
    x = 5
    y = 2
    result = x / y
except ZeroDivisionError:
    print("Division error")
else:
    print("Success! Result =", result)
finally:
    print("This always runs (e.g., clean up resources)")
