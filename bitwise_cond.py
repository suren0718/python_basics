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

# using bitwise opr log 1
n=int(input())

if((n & (n-1))==0):
  print("yes")
else:
  print("no")


# left shift multiply by 2
# right shift dividing by 2

n=int(input())

if(((n>>1)<<1) == n):
  print("even")

else:
  print("odd")
