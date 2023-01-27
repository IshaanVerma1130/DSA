def BinarySearch(arr, n, x):
    l = 0
    r = n - 1

    if arr[l] == arr[r]:
        return arr[l] if arr[l] == x else -1

    if arr[l] < arr[r]:
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

    else:
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                r = mid - 1
            else:
                l = mid + 1

    return -1


# Driver Code
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    x = 5
    print(BinarySearch(arr, n, x))
