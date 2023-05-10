def Solve(ones: int, zeroes: int, n: int, op: str):
    if n == 0:
        print(op)
        return

    op1 = op + "1"
    Solve(ones + 1, zeroes, n - 1, op1)

    if ones > zeroes:
        op2 = op + "0"
        Solve(ones, zeroes + 1, n - 1, op2)

    return


if __name__ == "__main__":
    n = 4
    op = ""
    Solve(0, 0, n, op)
