arr = [1, 7, 4, 2, 2, 5, 10, 9]


def selectionSort(arr):
    for i in range(len(arr)):
        lowest_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_index]:
                lowest_index = j

        if lowest_index != i:
            arr[i], arr[lowest_index] = arr[lowest_index], arr[i]


print(arr)
selectionSort(arr)
print(arr)
