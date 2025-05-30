"""2. Generators
A generator is a simpler way to create an iterator using yield instead of return.

Why Use Generators?

Saves memory — yields one item at a time

Used in data streaming, large datasets, pipelines, etc.

"""

def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)