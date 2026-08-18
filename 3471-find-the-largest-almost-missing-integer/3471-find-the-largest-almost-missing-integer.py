class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k==1:
            d={}
            for i in nums:
                d[i]=d.get(i,0)+1
            r=[i for i in d if d[i]==1]
            return max(r) if r else -1
        elif k==len(nums):
            return max(nums)
        else:
            d={}
            for i in nums:
                d[i]=d.get(i,0)+1
            if d[nums[0]]==1 and d[nums[-1]]==1:
                return max(nums[0],nums[-1])
            elif d[nums[0]]!=1 and d[nums[-1]]==1:
                return nums[-1]
            elif d[nums[-1]]!=1 and d[nums[0]]==1:
                return nums[0]
            else:
                return -1