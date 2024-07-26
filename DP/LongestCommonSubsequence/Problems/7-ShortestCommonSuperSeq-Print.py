def getString(dp: list[list[int]], x: str, y: str, n: int, m: int) -> str:
    i = n
    j = m
    string = []

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            string.append(x[i - 1])
            i -= 1
            j -= 1

        else:
            if dp[i][j - 1] > dp[i - 1][j]:
                string.append(y[j - 1])
                j -= 1
            else:
                string.append(x[i - 1])
                i -= 1

    while i > 0:
        string.append(x[i - 1])
        i -= 1

    while j > 0:
        string.append(y[j - 1])
        j -= 1

    return "".join(reversed(string))


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
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return getString(dp, x, y, n, m)


str1 = "ababa"
str2 = "cbbcad"

print(Solve(str1, str2, len(str1), len(str2)))
