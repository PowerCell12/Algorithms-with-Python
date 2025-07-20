rows = int(input())
columns = int(input())


matrix = [list(input()) for _ in range(rows)]

AreasDictionary = {}
checked = []

def dfs(matrix, i, j):

        if

        # if AreasDictionary[matrix[i][j]]:
        #     AreasDictionary[matrix[i][j]] += 1
        # else:
        #     AreasDictionary[matrix[i][j]] = 1


        dfs(matrix, i, j - 1)
        dfs(matrix, i, j + 1)
        dfs(matrix, i - 1, j)
        dfs(matrix, i + 1, j)



for i in range(columns):
    for j in range(rows):
        if matrix[i][j] != "v":
            dfs(matrix, i, j)
