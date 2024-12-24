list1 = list(map(int, input().split()))

def array_sum(list1):

    if len(list1) == 1:
        return list1[0]

    one = list1.pop()

    return one + array_sum(list1)



print(array_sum(list1))
