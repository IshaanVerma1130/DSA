def BinarySearch(arr):
    l = 0
    r = 1
    res = -1

    while arr[r] != 1:
        l = r
        r *= 2

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == 1:
            res = mid
            r = mid - 1

        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    arr = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ]
    print(BinarySearch(arr))
