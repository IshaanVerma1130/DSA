def Solve(wt, diff):
    if (sum(wt) + diff) % 2 != 0:  # Otherwise its not possible. think of an example
        return 0

    target = (sum(wt) + diff) // 2

    n = len(wt)
    m = target

    dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            if wt[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - wt[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]


wt = [0, 1, 2, 1, 3]
diff = 1
print(Solve(wt, diff))

"""
1. We only initialize the top left column of dp as it is the only certain answer
2. We start j from 0
"""
