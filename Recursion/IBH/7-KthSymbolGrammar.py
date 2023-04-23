def Solve(n, k):
    if n == 1 and k == 1:
        return 0

    mid = (2 ** (n - 1)) // 2

    if k <= mid:
        return Solve(n - 1, k)

    else:
        return Solve(n - 1, k - mid) ^ 1


if __name__ == "__main__":
    n = 4
    k = 7
    print(Solve(n, k))
