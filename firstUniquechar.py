from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)   # count frequencies
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
