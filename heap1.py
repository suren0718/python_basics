import heapq

def heaps(n):
  ts=0
  heapq.heapify(n)
  while(len(n)> 1):
    first=heapq.heappop(n)
    second=heapq.heappop(n)
    cs=first+second
    ts=ts+cs
    heapq.heappush(n, cs)
    
  return ts
num=[2, 4, 6, 3]
print(heaps(num))