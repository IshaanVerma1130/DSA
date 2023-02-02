def BinarySearch(arr, x):
    l = 0
    r = 1

    while arr[r] < x:
        l = r
        r *= 2

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid

        elif x < arr[mid]:
            r = mid - 1

        else:
            l = mid + 1

    return -1


if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    x = 140
    print((BinarySearch(arr, x)))
