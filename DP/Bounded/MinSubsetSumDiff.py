def SubsetSum(wt, w):
    n = len(wt)
    m = w

    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = False
            if j == 0:
                dp[i][j] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if wt[i - 1] <= w:
                dp[i][j] = dp[i - 1][j - wt[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    for i in dp:
        print(i)

    ans = []

    for i in range((w + 1) // 2):
        if dp[n][i]:
            ans.append(i)

    return ans


def Solve(wt):
    last_row_for_possible = SubsetSum(wt, sum(wt))

    rng = sum(wt)
    min_diff = 100000000
    for d in last_row_for_possible:
        min_diff = min(min_diff, rng - 2 * d)

    return min_diff


wt = [1, 2, 7]
print(Solve(wt))

"""
1. We need to find the minimum difference we can get after subtracting one subset from another
2. Let one subset be S1 and the other S2
3. We have to minimize S1 - S2
4. S2 is basically the sum of the elements of the array - S1
5. To make it simple we assume S2 is always bigger than S1, since we wont have to use mod then over S1 - (sum - S1)
6. So now we have to minimize S2 - S1 ~ Sum - 2*S1
7. Lets assume the range of S2 and S1, it can take values from 0 to Sum of Elements
8. For Example; [1, 2, 7]; Sum = 10; Range = [0:10]
9. Now we have to look at what value S1 and S2 can take, as not all elements form the range can be used;
    For Example:
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; the array [1, 2, 7] can only generate subsets of the sums [0, 1, 2, 3, 7, 8, 9, 10]
10. Now we have to find a way to get these out.
11. This can be done by using the last row of the dp matrix we get from solving SubsetSum as it tells us for which wt  we can get a subset from the array.
12. For each value that is True in the last row, we add it to the array till we reach the place where wt = sum/2
as we always want S2 to be greater than S1; the resultant array will give us the possible sum for S1
13. Then we get the minimum value for Sum - 2*S1
"""
