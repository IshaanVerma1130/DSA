dp = [[-1 for _ in range(10 + 1)] for i in range(10 + 1)]


def Solve(wt: list[int], val: list[int], w: int, n: int):
    if n == 0 or w == 0:
        return 0

    if dp[w][n] != -1:
        return dp[w][n]

    if wt[n - 1] <= w:
        dp[w][n] = max(
            val[n - 1] + Solve(wt, val, w - wt[n - 1], n - 1), Solve(wt, val, w, n - 1)
        )
        return dp[w][n]

    elif wt[n - 1] > w:
        dp[w][n] = Solve(wt, val, w, n - 1)
        return dp[w][n]


wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
w = 7

print(Solve(wt, val, w, len(wt)))
