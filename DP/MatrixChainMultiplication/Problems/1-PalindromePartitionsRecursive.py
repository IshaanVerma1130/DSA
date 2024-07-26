def isPalindrome(string):
    if string == string[::-1]:
        return True
    return False


def Solve(string, i, j):
    if i >= j:
        return 0

    if isPalindrome(string[i : j + 1]):
        return 0

    maxEl = 1000000000

    for k in range(i, j):
        temp = 1 + Solve(string, i, k) + Solve(string, k + 1, j)

        if temp < maxEl:
            maxEl = temp

    return maxEl


string = "abbac"
print(Solve(string, 0, len(string) - 1))
