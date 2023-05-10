def Solve(ip: str, op: str):
    if len(ip) == 0:
        print(op)
        return

    if ip[0].isdigit():
        op = op + ip[0]
        ip = ip[1:]
        Solve(ip, op)

    else:
        op1 = op + ip[0].lower()
        op2 = op + ip[0].upper()
        ip = ip[1:]
        Solve(ip, op1)
        Solve(ip, op2)

    return


if __name__ == "__main__":
    ip = "a1b2c3"
    op = ""

    Solve(ip, op)
