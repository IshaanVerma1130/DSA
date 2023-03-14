def PrintOneToN(n: int):
    if n == 1:
        print(1, end=" ")
        return

    PrintOneToN(n - 1)
    print(n, end=" ")


if __name__ == "__main__":
    PrintOneToN(7)
