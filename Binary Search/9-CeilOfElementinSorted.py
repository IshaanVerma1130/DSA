def BinarySearch(arr, n, x):
    l = 0
    r = n - 1
    res = -1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] > x:
            res = arr[mid]
            r = mid - 1

        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 8, 10, 12, 19]
    n = len(arr)
    x = 9
    print(BinarySearch(arr, n, x))
