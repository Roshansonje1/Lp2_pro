def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 9
result = binary_search(arr, target)

if result != -1:
    print("Target found at index", result)
else:
    print("Target not found")
