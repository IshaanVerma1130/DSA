def BinarySearch(arr, n, x):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        if arr[mid - 1] == x and mid > l:
            return mid - 1
        if arr[mid + 1] == x and mid < r:
            return mid + 1

        elif arr[mid] > x:
            r = mid - 2
        else:
            l = mid + 2

    return -1


if __name__ == "__main__":
    arr = [5, 10, 30, 20, 40]
    n = len(arr)
    x = 20
    print(BinarySearch(arr, n, x))
