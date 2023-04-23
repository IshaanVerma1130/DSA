def RecurSort(stack: list):
    if len(stack) == 1:
        return

    top = stack.pop()
    RecurSort(stack)
    Insert(stack, top)
    return


def Insert(stack: list, top: int):
    if len(stack) == 0 or stack[-1] <= top:
        stack.append(top)
        return

    temp = stack.pop()
    Insert(stack, top)
    stack.append(temp)
    return


if __name__ == "__main__":
    arr = [5, 3, 7, 9, 10, 2, 1]
    RecurSort(arr)
    print(arr)
