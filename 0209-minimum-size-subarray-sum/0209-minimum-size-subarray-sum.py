class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        s=0
        r=float("inf")
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                r=min(r, i-left+1)
                s-=nums[left]
                left+=1
        return r if r!=float("inf") else 0