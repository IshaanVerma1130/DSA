def BinarySearch(arr, n):
    l = 0
    r = n - 1

    while l <= r:
        mid = l + (r - l) // 2

        if mid > 0 and mid < n - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return arr[mid]
            elif arr[mid] < arr[mid + 1]:
                l = mid + 1
            else:
                r = mid - 1

        elif mid == 0:
            return arr[0] if arr[0] > arr[1] else arr[1]

        elif mid == n - 1:
            return arr[n - 1] if arr[n - 1] > arr[n - 2] else arr[n - 2]

    return -1


if __name__ == "__main__":
    arr = [2203, 5, 7, 9, 210, 90, 100, 1130, 1140, 1160, 170]
    n = len(arr)
    print((BinarySearch(arr, n)))
