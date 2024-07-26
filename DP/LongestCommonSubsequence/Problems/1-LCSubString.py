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
                dp[i][j] = 0

    maxEl = -1

    for i in range(n + 1):
        for j in range(m + 1):
            maxEl = max(maxEl, dp[i][j])

    return maxEl


str1 = "abcde"
str2 = "abfce"

print(Solve(str1, str2, len(str1), len(str2)))
