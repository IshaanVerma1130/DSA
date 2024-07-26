def Solve(wt):
    wt_sum = sum(wt)

    if wt_sum % 2 != 0:
        return False

    n = len(wt)
    m = wt_sum // 2

    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - wt[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


wt = [1, 5, 11, 5]
print(Solve(wt))
