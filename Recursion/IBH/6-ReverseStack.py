def Reverse(arr: list):
    if len(arr) == 1:
        return

    temp = arr.pop()
    Reverse(arr)
    Insert(arr, temp)
    return


def Insert(arr: list, ele: int):
    if len(arr) == 0:
        arr.append(ele)
        return

    temp2 = arr.pop()
    Insert(arr, ele)
    arr.append(temp2)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    Reverse(arr)
    print(arr)
