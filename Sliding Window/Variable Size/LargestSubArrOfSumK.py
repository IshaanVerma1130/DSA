def Solve(arr, k):
    i = j = 0
    sum = 0
    maxSize = 0

    while j < len(arr):
        sum += arr[j]

        if sum < k:
            j += 1

        elif sum == k:
            maxSize = max(maxSize, j - i + 1)
            j += 1

        else:
            while sum > k:
                sum -= arr[i]
                i += 1

            if sum == k:
                maxSize = max(maxSize, j - i + 1)
            j += 1

    return maxSize


print(Solve([1, 2, 3, 1, 1, 1, 1, 4, 0, 0, 2, 3], 5))
