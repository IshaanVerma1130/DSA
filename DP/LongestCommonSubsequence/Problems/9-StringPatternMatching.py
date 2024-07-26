# Check if str1 is a sub sequence of str2


def Solve(x: str, y: str, n: int, m: int) -> int:
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


str1 = "abc"
str2 = "axbyc"

print(True if Solve(str1, str2, len(str1), len(str2)) == len(str1) else False)
