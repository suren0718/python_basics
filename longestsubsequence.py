def subsequence(a, b):
  p=len(a)
  q=len(b)
  dp= [[0] * (q+1) for _ in range(p+1)]

  for i in range(1,p+1):
    for j in range(1, q+1):
      if a[i-1] == b[j-1]:
        dp[i][j] = 1+ dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
  return dp[p][q] #return the last row,col which has three 3(the max)

a="abcde"
b="ace"
print(subsequence(a, b))