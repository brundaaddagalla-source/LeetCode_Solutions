class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i]=abs(nums[i])
        r=0
        # while nums:
        #     r+=(nums.pop(nums.index(max(nums))))**2
        #     print(r)
        #     r-=(nums.pop(nums.index(min(nums))))**2
        #     print(r)
        # return r
        nums.sort()
        while len(nums)>1:
            r+=nums.pop()**2
            r-=nums.pop(0)**2
        if nums:
            r+=nums.pop()**2
        return r