def Solve(value):
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

    number = 0

    i = len(coins) - 1

    while value != 0 and i >= 0:
        if coins[i] > value:
            i -= 1
        else:
            value -= coins[i]
            number += 1

    print(number)


value = 49
Solve(value)
