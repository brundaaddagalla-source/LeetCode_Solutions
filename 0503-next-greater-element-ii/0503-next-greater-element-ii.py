class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        r=[]
        ans=[-1]*len(nums)
        for i in range(2*len(nums)):
            while r and nums[i%len(nums)] > nums[r[-1]]:
                ans[r.pop()] = nums[i%len(nums)]
            if i < len(nums):
                r.append(i)
        return ans