arr = list(map(int, input().split()))

def partitionAlgorithm(arr, pivot, i, j):
    while True:
        if j == len(arr):
            arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
            pivot = i + 1
            break

        if arr[j] < arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
        else:
            j += 1

    return pivot

def quickSort(arr, pivot, left, right):

    if left < right:

        pivot = partitionAlgorithm(arr, pivot, left, right)

        quickSort(arr, pivot, left, pivot - 1)
        quickSort(arr, pivot, pivot + 1, right)



quickSort(arr, len(arr) - 1, 0, len(arr) - 1)

print(arr)
