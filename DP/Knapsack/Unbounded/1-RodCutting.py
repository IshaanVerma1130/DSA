def Solve(wt, val):
    n = len(wt)
    m = len(val)

    dp = [[0 for _ in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j])

            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


length = [1, 2, 3, 4, 5, 6, 7, 8]
price = [1, 5, 8, 9, 10, 17, 17, 20]
print(Solve(length, price))
