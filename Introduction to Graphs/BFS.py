from collections import deque

adjArr =  [
    [3, 6],
    [3 ,6, 4, 2, 5],
    [1, 4, 5],
    [5, 1, 0],
    [1, 2, 6],
    [2, 1, 3],
    [0, 1, 4]
]

stack = []

def bfs(index, arr):

    if index not in stack:
        queue = deque()

        queue.append(index)
        stack.append(index)

        while queue:
            topNode = queue.popleft()
            print(topNode, end=" ")

            for childNode in arr[topNode]:

                if childNode not in stack:
                    stack.append(childNode)
                    queue.append(childNode)


for i in range(len(adjArr)):
    bfs(i, adjArr)
