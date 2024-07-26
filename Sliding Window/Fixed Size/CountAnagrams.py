def Solve(s, p):
    i = j = 0
    k = len(p)
    ans = []
    match = {}

    for ch in p:
        if ch not in match:
            match[ch] = 1
        else:
            match[ch] += 1

    count = len(match)

    while j < len(s):
        ch = s[j]
        if s[j] in match:
            match[s[j]] -= 1
            if match[s[j]] == 0:
                count -= 1

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            if count == 0:
                ans.append(i)

            if s[i] in match:
                match[s[i]] += 1
                if match[s[i]] == 1:
                    count += 1
            i += 1
            j += 1

    return ans


print(Solve("aabaa", "aa"))
