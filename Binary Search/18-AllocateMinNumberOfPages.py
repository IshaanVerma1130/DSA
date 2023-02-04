# Can be unsorted
def IsValid(arr, n, k, x):
    students = 1
    sum = 0

    for i in arr:
        sum += i
        if sum > x:
            students += 1
            sum = i

        if students > k:
            return False

    return True


def BinarySearch(arr, n, k):
    l = max(arr)
    r = sum(arr)
    res = -1

    if n < k:
        return -1

    while l <= r:
        mid = l + (r - l) // 2

        if IsValid(arr, n, k, mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(arr)
    k = 3
    print(BinarySearch(arr, n, k))
