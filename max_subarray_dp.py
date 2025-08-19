class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxsum=nums[0]
        currsum=nums[0]

        if currsum < 0:
            currsum =0

        for i in range(1, n):
            currsum += nums[i]
            maxsum = max(currsum, maxsum)

            if(currsum<0):
                currsum =0
        return maxsum
