class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p=-1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                if (nums[i]-1)*(nums[j]-1)>p:
                    p=(nums[i]-1)*(nums[j]-1)
        return p
        
