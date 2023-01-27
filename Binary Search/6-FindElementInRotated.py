def BinarySearch(arr, start, end, x):
    l = start
    r = end

    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1


def CalcTimes(arr, n):
    l = 0
    r = n - 1

    while l <= r:
        if arr[l] <= arr[r]:
            return l

        mid = l + (r - l) // 2

        next = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return mid

        elif arr[mid] <= arr[r]:
            r = mid - 1

        elif arr[mid] >= arr[l]:
            l = mid + 1


def FindElement(arr, n, x):
    min_element = CalcTimes(arr, n)

    left_side = BinarySearch(arr, 0, min_element - 1, x)
    right_side = BinarySearch(arr, min_element, n - 1, x)

    return left_side if left_side != -1 else right_side


if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    n = len(arr)
    x = 3

    print(FindElement(arr, n, x))
