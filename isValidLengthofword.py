class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs ={')' : '(', '}' : '{', ']':'[', }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack

# length of last words

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.rstrip()

        words= s.split()
        n=len(s)

        return len(words[-1])
