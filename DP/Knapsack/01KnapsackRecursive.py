def Solve(wt: list[int], val: list[int], w: int, n: int):
    if n == 0 or w == 0:
        return 0

    if wt[n - 1] <= w:
        return max(
            val[n - 1] + Solve(wt, val, w - wt[n - 1], n - 1), Solve(wt, val, w, n - 1)
        )

    elif wt[n - 1] > w:
        return Solve(wt, val, w, n - 1)


wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
w = 7

print(Solve(wt, val, w, len(wt)))
