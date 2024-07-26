arr = [1, 7, 4, 2, 2, 5, 10, 9]


def insertionSort(arr):
    for index in range(1, len(arr)):
        position = index
        temp_value = arr[index]

        while position > 0 and arr[position - 1] > temp_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = temp_value


print(arr)
insertionSort(arr)
print(arr)
