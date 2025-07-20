arr = list(map(int, input().split()))
searched = int(input())
left = 0
right = len(arr) - 1

def binary_search(arr, searched, left, right):
    mid_index = (left + right) // 2

    mid_element = arr[mid_index]

    if mid_element == searched:
        print(mid_index)
        return 1
    elif left > right:
        print(-1)
        return 1


    if mid_element < searched:
        left = mid_index + 1
    else:
        right = mid_index - 1

    binary_search(arr, searched, left, right)



binary_search(arr, searched, left, right)