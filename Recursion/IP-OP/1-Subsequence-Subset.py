def Solve(ip: str, op: str):
    if len(ip) == 0:
        print(op)
        return

    op1 = op
    op2 = op + ip[0]
    ip = ip[1:]

    Solve(ip, op1)
    Solve(ip, op2)
    return


if __name__ == "__main__":
    ip = "abc"
    op = ""
    Solve(ip, op)
