def RecurDelete(arr: list, k):
    if k == 1:
        arr.pop()
        return

    top = arr.pop()
    RecurDelete(arr, k - 1)
    arr.append(top)
    return


def Solve(arr: list, n):
    if n == 0:
        return
    k = (n + 1) // 2
    RecurDelete(arr, k)


if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6]
    n = len(arr)
    Solve(arr, n)
    print(arr)
