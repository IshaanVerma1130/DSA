# Min number of operations to calculate the Matrix Multiplication
dp = [[-1] * 1001 for i in range(1001)]


def Sovle(arr, i, j):
    if i >= j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    maxEl = 10000000000

    for k in range(i, j):
        temp = Sovle(arr, i, k) + Sovle(arr, k + 1, j) + arr[i - 1] * arr[k] * arr[j]

        if temp < maxEl:
            maxEl = temp
            dp[i][j] = maxEl

    return dp[i][j]


arr = [40, 20, 30, 10, 30]
print(Sovle(arr, 1, len(arr) - 1))
