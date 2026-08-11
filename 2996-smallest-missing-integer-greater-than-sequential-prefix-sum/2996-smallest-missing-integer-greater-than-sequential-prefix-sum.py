class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prev=-1
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                break
            else:
                curr+=nums[i]
        while curr in nums:
            curr+=1
        return curr