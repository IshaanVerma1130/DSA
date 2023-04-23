def Solve(n, s, d, h):
    if n == 1:
        print(f"Moving plate 1 from {s} to {d}")
        return

    Solve(n - 1, s, h, d)
    print(f"Moving plate {n} from {s} to {d}")
    Solve(n - 1, h, d, s)


if __name__ == "__main__":
    n = 10
    Solve(n, "A", "B", "C")
