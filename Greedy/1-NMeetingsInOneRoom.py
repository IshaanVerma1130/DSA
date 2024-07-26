def Solve(s: list[int], f: list[int]) -> int:
    arr = []
    for i in range(len(s)):
        arr.append([s[i], f[i], i + 1])

    arr.sort(key=lambda x: x[1])

    answer = [arr[0][2]]
    limit = arr[0][1]

    for i in range(1, len(arr)):
        if arr[i][0] > limit:
            limit = arr[i][1]
            answer.append(arr[i][2])

    print(answer)


s = [1, 0, 3, 8, 5, 8]
f = [2, 6, 4, 9, 7, 9]

Solve(s, f)
