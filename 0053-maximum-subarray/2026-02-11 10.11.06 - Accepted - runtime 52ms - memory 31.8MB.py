class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=c=nums[0]
        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            maxi=max(c,maxi)
        return maxi