def First(arr, n, x):
    l = 0
    r = n - 1
    res = -1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            res = mid
            r = mid - 1
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1

    return res


def Last(arr, n, x):
    l = 0
    r = n - 1
    res = -1

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            res = mid
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 5, 5, 6, 7]
    n = len(arr)
    x = 5
    print(First(arr, n, x))
    print(Last(arr, n, x))
