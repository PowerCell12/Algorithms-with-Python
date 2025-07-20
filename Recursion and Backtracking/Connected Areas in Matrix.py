row = int(input())
column = int(input())
matrix = []

for i in range(row):
    matrix.append(list(input()))


def exploreArea(currentRow, currentColumn, matrix):

    if currentRow == row or currentColumn == column or currentRow < 0 or currentColumn < 0 or matrix[currentRow][currentColumn] == "*" or matrix[currentRow][currentColumn] == "v":
        return 0

    matrix[currentRow][currentColumn] = "v"

    result = 1
    result += exploreArea(currentRow, currentColumn - 1, matrix)
    result += exploreArea(currentRow, currentColumn + 1, matrix)
    result += exploreArea(currentRow - 1, currentColumn, matrix)
    result += exploreArea(currentRow + 1, currentColumn, matrix)

    return result

count = 0
dictInit = {}

for i in range(row):
    for j in range(column):
        size = exploreArea(i, j, matrix)
        if (size != 0):
            count += 1
            dictInit[count] = [size, i, j]

dictFinal = dict(sorted(dictInit.items(), key=lambda x: -x[1][0]))
count = 0

print(f"Total areas found: {len(dictFinal)}")
for value in dictFinal.values():
    count += 1
    print(f"Area #{count} at ({value[1]}, {value[2]}), size: {value[0]}")
