def Solve(wt, w):
    n = len(wt)
    m = w

    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - wt[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]


wt = [2, 3, 5, 8, 6, 10]
w = 10
print(Solve(wt, w))
