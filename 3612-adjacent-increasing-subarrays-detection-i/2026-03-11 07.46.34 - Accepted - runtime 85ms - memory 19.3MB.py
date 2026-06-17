class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)-2*k+1):
            x=nums[i:i+k]
            y=nums[i+k:i+k+k]
            def check(x):
                for i in range(len(x)-1):
                    if x[i]>=x[i+1]:
                        return False
                return True
            if check(x) and check(y):
                return True
        return False