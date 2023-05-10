def Solve(open: int, close: int, op: str):
    if open == 0 and close == 0:
        print(op)
        return

    if open != 0:
        op1 = op + "("
        Solve(open - 1, close, op1)

    if close > open:
        op2 = op + ")"
        Solve(open, close - 1, op2)

    return


if __name__ == "__main__":
    n = 3
    op = ""

    Solve(n, n, op)
