class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l=set()
        r=[]
        for i in nums:
            if i in l:
                r.append(i)
            else:
                l.add(i)
        return r