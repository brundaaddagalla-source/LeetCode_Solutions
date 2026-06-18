class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left=0
        r=0
        p=1
        for i in range(len(nums)):
            p*=nums[i]
            while p>=k:
                p//=nums[left]
                left+=1
            r+=i-left+1
        return r

#https://www.youtube.com/watch?v=2M00YGmT9lM