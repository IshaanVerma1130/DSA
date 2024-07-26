def Solve(s, p):
    i = j = 0
    mp = {}
    minLen = len(s) + 1
    ans = []

    for ch in p:
        if ch in mp:
            mp[ch] += 1
        else:
            mp[ch] = 1

    count = len(mp)

    while j < len(s):
        if s[j] in mp:
            mp[s[j]] -= 1

            if mp[s[j]] == 0:
                count -= 1

        if count == 0:
            while count == 0:
                if j - i + 1 < minLen:
                    minLen = j - i + 1
                    ans = s[i : j + 1]
                if s[i] in mp:
                    mp[s[i]] += 1

                    if mp[s[i]] == 1:
                        count += 1

                i += 1

        j += 1

    return ans if len(ans) != 0 else ""


print(Solve("cabwefgewcwaefgcf", "cae"))
