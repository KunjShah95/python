""" 1. Iterators
An iterator is any object with:

__iter__() method → returns the iterator object

__next__() method → returns the next item or raises StopIteration"""

nums ={1, 2, 3, 4, 5}
itr = iter(nums)

print(next(itr))  # Output: 1
print(next(itr))  # Output: 2
print(next(itr))  # Output: 3
print(next(itr))  # Output: 4   
print(next(itr))  # Output: 5


class CountDown:
    def __init__(self, start):
        self.num= start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        val = self.num
        self.num -= 1
        return val

for i in CountDown(5):
    print(i)  # Output: 5, 4, 3, 2, 1        