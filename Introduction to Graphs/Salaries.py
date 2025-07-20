from collections import deque

rows = int(input())

matrix = [list(input()) for _ in range(rows)]


checked = {}

def bfs(matrix, index):
        queue = deque()

        checked[index] = 1
        queue.append(index)

        while queue:
            index = queue.popleft()

            for j in range(len(matrix[index])):
                child = matrix[index][j]

                if child == "Y":
                    if j not in checked:
                        bfs(matrix, j)

                        checked[index] -= 1

                    checked[index] += checked[j]


for i in range(rows):
    bfs(matrix, i)

print(checked)