class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[1]*len(nums)
        pre=post=1
        for i in range(len(nums)):
            r[i]=r[i]*pre
            pre=pre*nums[i]
            r[len(nums)-i-1]=r[len(nums)-i-1]*(post)
            post=post*nums[len(nums)-i-1]
        return r