def Solve(arr, k):
    i = j = 0
    helper = []

    while j < len(arr):
        while len(helper) > 0 and helper[-1] < arr[j]:
            helper.pop()

        helper.append(arr[j])

        if j - i + 1 < k:
            j += 1

        elif j - i + 1 == k:
            print(helper[0])

            if helper[0] == arr[i]:
                helper.pop(0)

            i += 1
            j += 1


Solve([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)
