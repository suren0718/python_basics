ways=0

def totalNqueens(n):
  global ways
  ways=0
  rowf= [False] * n
  colf =[False] * n
  t1df = [False] *(2 * n + 1)
  t2df = [False] *(2 * n + 1)
  fill(n, 0, rowf, colf, t1df, t2df)
  return ways 

def fill(n, row, rowf, colf, t1df, t2df):
  global ways
  if row == n:
    ways += 1
    return

  for col in range(n):
    if not rowf[row] and not colf[col] and not t1df[row -col + n] and not t2df[row + col]:

      rowf[row] = colf[col] = t1df[row-col +n] = t2df[row + col] =True

      fill(n, row+1, rowf, colf, t1df, t2df)

      rowf[row] = colf[col]= t1df[row-col+n] = t2df[row+col] = False

print(totalNqueens(4))