def RecurSort(arr: list):
    if len(arr) == 1:
        return

    temp = arr.pop()
    RecurSort(arr)
    Insert(arr, temp)
    return


def Insert(arr: list, temp: int):
    if len(arr) == 0 or arr[-1] <= temp:
        arr.append(temp)
        return

    temp_val = arr.pop()
    Insert(arr, temp)
    arr.append(temp_val)
    return


if __name__ == "__main__":
    arr = [5, 3, 7, 9, 10, 2, 1]
    RecurSort(arr)
    print(arr)
