array = input().split(" ")
rev_arr = []

def reverseArray(arr):
  if len(arr) == 1:
    rev_arr.append(arr[0])
    return 1

  reverseArray(arr[1:])

  rev_arr.append((arr[0]))


reverseArray(array)
print(" ".join(rev_arr))
