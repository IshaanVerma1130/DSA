def Solve(arr):
    i = j = 0
    maxLen = -1
    mp = dict()

    while j < len(arr):
        if arr[j] not in mp:
            mp[arr[j]] = 1
        else:
            mp[arr[j]] += 1

        if len(mp) == j - i + 1:
            maxLen = max(maxLen, j - i + 1)
            j += 1

        elif len(mp) < j - i + 1:
            while len(mp) < j - i + 1:
                mp[arr[i]] -= 1

                if mp[arr[i]] == 0:
                    mp.pop(arr[i])

                i += 1
            j += 1

    return maxLen


print(Solve("aabacbebebedd"))
