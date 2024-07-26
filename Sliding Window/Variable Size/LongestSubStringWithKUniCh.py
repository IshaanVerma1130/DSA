def Solve(s, k):
    i = j = 0
    chMap = {}
    maxLen = -1

    while j < len(s):
        if s[j] not in chMap:
            chMap[s[j]] = 1
        else:
            chMap[s[j]] += 1

        if len(chMap) < k:
            j += 1

        elif len(chMap) == k:
            maxLen = max(maxLen, j - i + 1)
            j += 1

        elif len(chMap) > k:
            while len(chMap) > k:
                chMap[s[i]] -= 1

                if chMap[s[i]] == 0:
                    chMap.pop(s[i])

                i += 1

            j += 1
    return maxLen


print(Solve("aabacbebebedd", 3))
