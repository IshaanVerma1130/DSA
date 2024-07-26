def Solve(arr):
    arr.sort(key=lambda x: x[2], reverse=True)

    mxDeadline = 0
    for i in arr:
        mxDeadline = max(mxDeadline, i[1])

    results = [-1] * (mxDeadline + 1)

    countJobs = 0
    jobProfit = 0

    for i in range(len(arr)):
        for j in range(arr[i][1], 0, -1):
            if results[j] == -1:
                results[j] = arr[i][0]
                jobProfit += arr[i][2]
                countJobs += 1
                break

    return [countJobs, jobProfit]


arr = [
    [1, 4, 20],
    [2, 5, 60],
    [3, 6, 70],
    [4, 6, 65],
    [5, 4, 25],
    [6, 2, 80],
    [7, 2, 10],
    [8, 2, 20],
]

print(Solve(arr))
