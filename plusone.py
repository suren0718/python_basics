class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        num = int("".join(map(str, digits)))

        num+=1

        dig =  [int(d) for d in str(num)]
        return dig
