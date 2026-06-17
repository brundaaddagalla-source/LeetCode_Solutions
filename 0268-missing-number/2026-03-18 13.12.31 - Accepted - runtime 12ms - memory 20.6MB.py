class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        i=0
        if len(nums)==1:
            if nums[0]!=0:
                return 0
            else:
                return 1
        while i<len(nums)-1:
            if nums[0]!=0:
                return 0
            if nums[i+1]!=nums[i]+1:
                return (nums[i+1]+nums[i])//2
            i+=1
        return nums[-1]+1