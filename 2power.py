# matrix dyanamic programming

rows=int(input())
cols=int(input())
matrix =[]

for i in range(rows):
  row=[]
  for j in range(cols):
    value=int(input())
    row.append(value)
  matrix.append(row)

for j in range(1, cols):
  matrix[0][j] = matrix[0][j-1]+ matrix[0][j]

for i in range(1, rows):
  matrix[i][0] = matrix[i-1][0] + matrix[i][0]

for i in range(1,rows):
  for j in range(1, cols):
    matrix[i][j] += max(matrix[i-1][j], matrix[i][j-1])

print(matrix[rows-1][cols-1])
