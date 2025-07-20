arr = list(map(int, input().split()))

for i in range(len(arr)):
    for j in range(i - 1, -1, -1):

        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i -= 1
        else:
            break

print(" ".join(list(map(str, arr))))
