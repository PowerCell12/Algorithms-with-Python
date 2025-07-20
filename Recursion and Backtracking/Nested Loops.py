number = int(input())
arr = [1 for _ in range(number)]

idx = 0


def nestedLoops(arr, idx):

  if idx == len(arr):
    print(" ".join(list(map(str, arr))))
    idx = idx - 1
    return 1

  for i in range(1, number + 1):
    arr[idx] = i


    nestedLoops(arr, idx + 1)

  idx = idx - 1


nestedLoops(arr, idx)
