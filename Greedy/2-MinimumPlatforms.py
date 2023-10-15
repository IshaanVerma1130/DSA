def Solve(s: list[int], f: list[int]) -> int:
    s.sort()
    f.sort()

    plat = 1
    maxPlats = 1

    arrival = 1
    departure = 0

    while arrival < len(s):
        if s[arrival] <= f[departure]:
            plat += 1
            arrival += 1

        elif s[arrival] > f[departure]:
            plat -= 1
            departure += 1

        maxPlats = max(plat, maxPlats)

    return maxPlats


s = [900, 940, 950, 1100, 1500, 1800]
f = [910, 1200, 1120, 1130, 1900, 2000]

print(Solve(s, f))
