dp = [[-1] * 10 for _ in range(10)]


def Solve(x: str, y: str, n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0

    if dp[n][m] != -1:
        return dp[n][m]

    if x[n - 1] == y[n - 1]:
        dp[n][m] = 1 + Solve(x, y, n - 1, m - 1)
        return dp[n][m]

    else:
        dp[n][m] = max(Solve(x, y, n - 1, m), Solve(x, y, n, m - 1))
        return dp[n][m]


str1 = "abcdgh"
str2 = "abedfhr"

print(Solve(str1, str2, len(str1), len(str2)))
