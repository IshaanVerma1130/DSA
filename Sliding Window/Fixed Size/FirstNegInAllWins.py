def Solve(arr, k):
    i = j = 0
    ans = []

    while j < len(arr):
        if arr[j] < 0:
            ans.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if len(ans) == 0:
                print(0)
            else:
                print(ans[0])
                if arr[i] == ans[0]:
                    ans.pop(0)
            i += 1
            j += 1


Solve([12, -1, -7, 8, -15, 30, 16, 28], 3)
