def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("Linear Search:", linear_search([4, 2, 7, 1], 7))  # Output: 2
