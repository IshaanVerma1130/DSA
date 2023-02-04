def MaxInBitonic(arr, n):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        elif arr[mid] < arr[mid - 1]:
            r = mid - 1

        else:
            l = mid + 1


def BinarySearch(arr, start, end, x):
    l = start
    r = end

    if arr[l] < arr[r]:
        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] < x:
                l = mid + 1

            elif arr[mid] > x:
                r = mid - 1

    else:
        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid] == x:
                return mid

            elif arr[mid] < x:
                r = mid - 1

            elif arr[mid] > x:
                l = mid + 1

    return -1


def Search(arr, n, x):
    max_element = MaxInBitonic(arr, n)

    left_side = BinarySearch(arr, 0, max_element, x)
    right_side = BinarySearch(arr, max_element + 1, n - 1, x)

    if left_side != -1:
        return left_side
    if right_side != -1:
        return right_side
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 70, 28, 23, 22, 20]
    n = len(arr)
    x = 5
    print((Search(arr, n, x)))
