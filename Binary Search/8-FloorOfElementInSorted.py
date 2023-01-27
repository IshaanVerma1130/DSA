def BinarySearch(arr, n, x):
    l = 0
    r = n - 1
    res = -1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return arr[mid]

        if arr[mid] < x:
            l = mid + 1
            res = arr[mid]
        else:
            r = mid - 1

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 8, 10, 12, 19]
    n = len(arr)
    x = 10
    print(BinarySearch(arr, n, x))
