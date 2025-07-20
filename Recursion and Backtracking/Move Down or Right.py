row = int(input())
column = int(input())
matrix = [[0 for j in range(column)] for _ in range(row)]

current_row = 0
current_column = 0
count = [0]

def LadyBug(matrix, current_row, current_column, count):

  if current_row == len(matrix) or current_column == len(matrix[current_row]):
    return 1

  if current_row == row - 1 and current_column == column - 1:
    count[0] += 1
    return 1

  LadyBug(matrix,current_row, current_column + 1, count)
  LadyBug(matrix, current_row + 1, current_column, count)


LadyBug(matrix, current_row, current_column, count)
print(count[0])
