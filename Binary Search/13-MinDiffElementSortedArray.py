def BinarySearch(arr, n, x):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return arr[mid]

        elif arr[mid] > x:
            r = mid - 1

        else:
            l = mid + 1

    min_left = abs(arr[l] - x)
    min_right = abs(arr[r] - x)

    return arr[l] if min_left < min_right else arr[r]


if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    n = len(arr)
    x = 118
    print((BinarySearch(arr, n, x)))
