def Solve(wt, w):
    n = len(wt)
    m = w

    dp = [[0 for _ in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = dp[i][j - wt[i - 1]] + dp[i - 1][j]

            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


coins = [1, 2, 3]
sum = 5
print(Solve(coins, sum))
