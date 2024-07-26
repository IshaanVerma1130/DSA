def Solve(x: str, y: str, n: int, m: int) -> int:
    if n == 0 or m == 0:
        return 0

    if x[n - 1] == y[n - 1]:
        return 1 + Solve(x, y, n - 1, m - 1)

    else:
        return max(Solve(x, y, n - 1, m), Solve(x, y, n, m - 1))


str1 = "abcdgh"
str2 = "abedfhr"

print(Solve(str1, str2, len(str1), len(str2)))
