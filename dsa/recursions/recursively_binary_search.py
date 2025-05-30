def binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

nums = [10, 20, 30, 40, 50]
print("Index of 30:", binary_search(nums, 30, 0, len(nums)-1))  # 2
