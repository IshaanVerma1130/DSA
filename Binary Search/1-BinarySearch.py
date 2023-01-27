def BinarySearch(arr, n, x):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1


# Driver Code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    x = 10
    n = len(arr)

    result = BinarySearch(arr, n, x)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in array")
