string=input()
n=len(string)
result=[]

for i in range(1, n):
  sub=""
  for j in range(n):
    if i & (1<<j)