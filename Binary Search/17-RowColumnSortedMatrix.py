def BinarySearch(arr, n, m, x):
    i = 0
    j = m - 1

    while i < n and j >= 0:
        if arr[i][j] == x:
            return (i, j)

        elif arr[i][j] < x:
            i += 1

        elif arr[i][j] > x:
            j -= 1

    return -1


if __name__ == "__main__":
    arr = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 95], [32, 33, 39, 150]]
    n = len(arr)
    m = len(arr[0])
    x = 40
    print(BinarySearch(arr, n, m, x))
