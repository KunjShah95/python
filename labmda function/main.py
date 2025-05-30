#syntax
''' lambda arguments: expression '''

#basic lambda function
def square(x):
	return x ** 2
print(square(5))  # Output: 25

# Lambda function with multiple arguments
def add(x, y):
	return x + y
print(add(3, 4))  # Output: 7

#using lambda inside sorted()
points = [(1, 2), (3, 1), (5, 4), (2, 2)]

# Sort points by y-coordinate
points_sorted = sorted(points, key=lambda point: point[1])
print(points_sorted)  # Output: [(3, 1), (1, 2), (2, 2), (5, 4)]
