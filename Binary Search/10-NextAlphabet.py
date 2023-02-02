def BinarySearch(arr, n, x):
    l = 0
    r = n - 1
    res = -1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            l = mid + 1

        elif x < arr[mid]:
            res = arr[mid]
            r = mid - 1

        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    arr = ["a", "e", "f", "h", "l"]
    n = len(arr)
    x = "h"
    print(BinarySearch(arr, n, x))
