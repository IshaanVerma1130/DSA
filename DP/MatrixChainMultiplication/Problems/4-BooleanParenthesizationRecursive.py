def Solve(string, i, j, isTrue):
    if i > j:
        return 0

    if i == j:
        if isTrue == True:
            if string[i] == "T":
                return 1
            else:
                return 0

        elif isTrue == False:
            if string[i] == "F":
                return 1
            else:
                return 0

    ans = 0

    for k in range(i + 1, j, 2):
        lF = Solve(string, i, k - 1, False)
        lT = Solve(string, i, k - 1, True)
        rF = Solve(string, k + 1, j, False)
        rT = Solve(string, k + 1, j, True)

        if string[k] == "&":
            if isTrue == True:
                ans += lT * rT
            else:
                ans += lF * rT + lF * rF + lT * rF

        elif string[k] == "|":
            if isTrue == True:
                ans += rT * lF + rT * lT + lT * rF
            else:
                ans += rF * lF

        elif string[k] == "^":
            if isTrue == True:
                ans += lF * rT + lT * rF
            else:
                ans += lF * rF + rT * lT

    return ans


string = "T|T&F^T"
print(Solve(string, 0, len(string) - 1, True))
