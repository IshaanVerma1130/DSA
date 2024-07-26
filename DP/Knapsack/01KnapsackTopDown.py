def Solve(wt, val, w):
    n = len(wt)
    m = w
    dp = [[-1 for _ in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]], dp[i - 1][j])

            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


wt = [1, 3, 4, 5]
val = [1, 4, 5, 7]
w = 7

print(Solve(wt, val, w))
