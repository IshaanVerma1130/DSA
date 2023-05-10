def Solve(ip: str, op: str):
    if len(ip) == 0:
        print(op)
        return

    op1 = op + ip[0]
    op2 = op + ip[0].upper()
    ip = ip[1:]

    Solve(ip, op1)
    Solve(ip, op2)


if __name__ == "__main__":
    ip = "ab"
    op = ""

    Solve(ip, op)
