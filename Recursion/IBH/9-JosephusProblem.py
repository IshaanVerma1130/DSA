def Solve(arr: list, k: int, index: int):
    if len(arr) == 1:
        print(arr[0])
        return

    index = (index + k) % len(arr)
    arr.pop(index)
    Solve(arr, k, index)
    return


if __name__ == "__main__":
    n = 40
    arr = [i + 1 for i in range(n)]
    k = 7
    index = 0
    Solve(arr, k - 1, index)
