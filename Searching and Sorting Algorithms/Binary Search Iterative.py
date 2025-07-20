arr = list(map(int, input().split()))
searched = int(input())

def binary_search(arr, searched):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid_index = (left + right) // 2

    mid_element = arr[mid_index]

    if mid_element == searched:
      return mid_index
    elif mid_element > searched:
      right = mid_index - 1
    else:
      left = mid_index + 1

  return -1

print(binary_search(arr, searched))