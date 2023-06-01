def OABinarySearch(arr, n, x):
    l = 0
    r = n - 1

    if arr[l] == arr[r]:
        return l if arr[l] == x else -1

    if arr[l] < arr[r]:
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1

    else:
        while l <= r:
            mid = r + (l - r) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] < x:
                r = mid - 1
            else:
                l = mid + 1

    return -1


# Driver Code
if __name__ == "__main__":
    arr = [7, 6, 5, 4, 3, 2, 1]
    n = len(arr)
    x = 5
    print(OABinarySearch(arr, n, x))
