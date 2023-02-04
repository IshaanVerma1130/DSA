def BinarySearch(arr, n):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]

        elif arr[mid] < arr[mid - 1]:
            r = mid - 1

        else:
            l = mid + 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 3, 2, 1]
    n = len(arr)
    print(BinarySearch(arr, n))
