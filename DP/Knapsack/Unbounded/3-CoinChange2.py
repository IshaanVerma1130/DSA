def Solve(wt, w):
    n = len(wt)
    m = w

    dp = [[0 for _ in range(m + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = 10000
            if j == 0:
                dp[i][j] = 0
            if i == 1 and j >= 1:
                if j % wt[0] == 0:
                    dp[i][j] = j // wt[0]
                else:
                    dp[i][j] = 10000

    for i in range(2, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = min(dp[i][j - wt[i - 1]] + 1, dp[i - 1][j])

            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


coins = [1, 2, 3]
sum = 5
print(Solve(coins, sum))
