# print power of 2

n = int(input())
for i in range(1, n+1):
  print(2**i)

#find a no. is power of 2 or not time(log n)

n=int(input())

while(n%2 == 0):
  n=n/2

if(n==1):
  print("yes")
else:
  print("no")
