class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for i in queries:
            idx=i[0]
            while idx<=i[1]:
                nums[idx]=(nums[idx]*i[3])%((10**9)+7)
                idx+=i[2]
        r=nums[0]
        for i in range(1,len(nums)):
            r=r^nums[i]
        return r
        