def longest_balanced(nums):
  prefix_sum = 0
  seen = {0: -1}
  max_len = 0
  vow=["a","e","i","o","u"]
  for i, val in enumerate(nums):
    prefix_sum +=1 if val in vow else -1

    if prefix_sum in seen:
      max_len=max(max_len, i-seen[prefix_sum])
    
    else:
      seen[prefix_sum]=i

  return max_len

nums="aeroplan"
print(longest_balanced(nums))