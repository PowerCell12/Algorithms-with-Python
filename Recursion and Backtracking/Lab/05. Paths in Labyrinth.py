rows = int(input())
column = int(input())

lab = []

for _ in range(rows):
    lab.append(list(input()))


def FindAllPaths(rowIndx, colIdx, matrix, path="", direction=""):
    if (rowIndx < 0 or colIdx < 0 or rowIndx >= len(matrix) or colIdx >= len(matrix[0])):
        return

    if matrix[rowIndx][colIdx] == "e":
        direction += path
        print(direction)
        direction = direction[:-1]
        return

    if (matrix[rowIndx][colIdx]) == "*":
        return

    if (matrix[rowIndx][colIdx] == "v"):
        return

    matrix[rowIndx][colIdx] = "v"
    direction += path

    FindAllPaths(rowIndx - 1, colIdx, matrix,   "U", direction)
    FindAllPaths(rowIndx + 1, colIdx, matrix,  "D", direction)
    FindAllPaths(rowIndx, colIdx - 1, matrix, "L", direction)
    FindAllPaths(rowIndx, colIdx + 1, matrix, "R", direction)

    direction = direction[:-1]
    matrix[rowIndx][colIdx] = "-"


FindAllPaths(0,0, lab)


