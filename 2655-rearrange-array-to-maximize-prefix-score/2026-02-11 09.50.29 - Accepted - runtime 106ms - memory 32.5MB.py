class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums=sorted(nums,reverse=True)
        l=[0]*len(nums)
        l[0]=nums[0]
        for i in range(1,len(nums)):
            l[i]=nums[i]+l[i-1]
        f=[i for i in l if i>0]
        return(len(f))
        