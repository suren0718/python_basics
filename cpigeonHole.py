n, q =(map(int, input().split()))

pig_pos =[i for i in range(n+1)]

nest_count = [1] * (n+1)

overlap_count=0

for _ in range(q):
  query = input().split()

  if query[0] == "1":
    p, h = int(query[1]), int(query[2])  #getting p and h
    old=pig_pos[p]                       #current nest of pigeon

    nest_count[old] -=1                  #reducing nest count of p which is h1 

    if nest_count[old] == 1:             #from 2 to 1 so reducing multiple pigeon holes count
      overlap_count -=1

    nest_count[h] +=1                    # h is the target hole and inc +1 
    if nest_count[h] == 2:               #and also multiple_count +1
      overlap_count +=1
    
    pig_pos[p] = h                       #update the pigeon pos
  else:
    print(overlap_count)

