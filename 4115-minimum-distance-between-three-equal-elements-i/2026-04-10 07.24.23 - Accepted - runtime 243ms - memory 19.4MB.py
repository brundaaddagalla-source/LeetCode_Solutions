class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        x=float('inf')
        n=len(nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]==nums[j]==nums[k]:
                        dist=abs(i-j)+abs(j-k)+abs(k-i)
                        x=min(x,dist)
        return x if x != float('inf') else -1
        