arr = list(map(int, input().split()))

for i in range(len(arr)):
    element = arr[i]

    lowest = element
    index = i

    for j in range(i + 1, len(arr)):
        innerElement = arr[j]

        if (innerElement < lowest):
            lowest = innerElement
            index = j


    if index != i:
        arr[index] = arr[i]
        arr[i] = lowest


print(" ".join(list(map(str, arr))))