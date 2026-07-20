class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        r=[]
        for i in d:
            if d[i]==1:
                r.append(i)
        return r