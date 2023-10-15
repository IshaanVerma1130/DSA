dp = [[-1] * 1001 for i in range(1001)]


def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False


def Solve(string, i, j):
    if i >= j:
        return 0

    if isPalindrome(string[i : j + 1]):
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    maxEl = 1000000000

    for k in range(i, j):
        temp = 1 + Solve(string, i, k) + Solve(string, k + 1, j)

        if temp < maxEl:
            maxEl = temp
            dp[i][j] = maxEl

    return dp[i][j]


string = "nitik"
print(Solve(string, 0, len(string) - 1))
