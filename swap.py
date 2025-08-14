# Get array from user
def rotate(arr, k):
  n=len(arr)
  k=k%n
   
  def reverse(left, right):   
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # swap without temp
        left += 1
        right -= 1
  reverse(0, n-1)
  reverse(0,k-1)
  reverse(k, n-1)



arr = list(map(int, input().split()))
r=int(input())
rotate(arr, r)
print(arr)