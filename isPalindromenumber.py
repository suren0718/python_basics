class Solution:
    def isPalindrome(self, x: int) -> bool:
        li = str(x)
        left = 0
        right = len(li) - 1
        
        while left < right:  # compare digits from both ends
            if li[left] != li[right]:
                return False
            left += 1
            right -= 1
        
        return True
