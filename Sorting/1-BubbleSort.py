arr = [1, 7, 4, 2, 2, 5, 10, 9]


def bubbleSort(arr):
    unsorted_until_index = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True

        for i in range(unsorted_until_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted = False

        unsorted_until_index -= 1


print(arr)
bubbleSort(arr)
print(arr)
