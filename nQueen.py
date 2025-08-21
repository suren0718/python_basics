def nQueen(n):
  dp=[[0] * n for _ in range(n)]
  row=len(dp)
  col=len(dp[0])  
  
  for r in range(row):
    for c in range(col):
      if 


n=4
print(nQueen(n))