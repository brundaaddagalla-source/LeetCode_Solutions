class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        c=0
        while i<len(nums):
            if i>c:
                return False
            c=max(c, i+nums[i])
            if c>=len(nums)-1:
                return True
            i+=1
        return True