class Solution:
    def findLHS(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        keys=sorted(list(d.keys()))
        c=0
        for i in range(1,len(keys)):
            if keys[i]-keys[i-1]==1:
                c=max(c, d[keys[i]]+d[keys[i-1]])
        return c
