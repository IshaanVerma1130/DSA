import sys


def Solve(arr, k):
    sum = 0
    maxSum = -sys.maxsize
    i = j = 0

    while j < len(arr):
        sum += arr[j]

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            maxSum = max(maxSum, sum)
            sum -= arr[i]
            i += 1
            j += 1

    return maxSum


print(Solve([1, 4, 2, 6, 8, 3, 2, 6], 4))
