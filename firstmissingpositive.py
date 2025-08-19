class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
    #     nums.sort()
    #     mex = 1
    #     for num in nums:
    #         if num == mex:
    #             mex += 1
    #     return mex

    
        num_set = set(nums)  # acts like a map for presence
        mex = 1
        while mex in num_set:
            mex += 1
        return mex
