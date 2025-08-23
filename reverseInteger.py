class Solution:
    def reverse(self, x: int) -> int:
        # set limit for 32-bit signed integer
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  

        # check sign
        neg = x < 0
        x = abs(x)

        # reverse by string slicing
        rev = int(str(x)[::-1])

        if neg:
            rev = -rev

        # check overflow
        if rev < INT_MIN or rev > INT_MAX:
            return 0

        return rev
