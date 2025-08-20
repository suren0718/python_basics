n=int(input())
num= 1

for i in range(1, n+1):
  if i<=(n+1)//2:
    count=i
  else:
    count = n- i +1

  row_nums =[]
  for j in range(count):
    row_nums.append(num+j)
  
  num +=count

  print(" ".join(map(str, row_nums[::-1])))


  