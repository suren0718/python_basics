def binarysearch(nums, target):
  n = len(nums)
  for i in range(0, n):
    if nums[i]== target:
      return i
      

    elif nums[i] != target:
      return target-1

nums=[0,1,2,4]
target=3
print(binarysearch(nums, target))
