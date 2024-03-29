# Check both left and right sides
def CalcTimes(arr, n):
    l = 0
    r = n - 1

    if arr[l] <= arr[r]:
        return 0

    while l <= r:
        mid = l + (r - l) // 2

        next = (mid + 1) % n
        prev = (mid + n - 1) % n

        if arr[mid] <= arr[next] and arr[mid] <= arr[prev]:
            return n - mid

        elif arr[mid] <= arr[r]:
            r = mid - 1

        elif arr[mid] >= arr[l]:
            l = mid + 1


if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2]
    n = len(arr)
    print(CalcTimes(arr, n))
