arr = list(map(int, input().split()))



for j in range(len(arr)):
    swaps  = 0

    for i in range(1, len(arr)  - j):
        j = i - 1

        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            swaps += 1


    if swaps == 0:
        break


print(" ".join(list(map(str, arr))))
