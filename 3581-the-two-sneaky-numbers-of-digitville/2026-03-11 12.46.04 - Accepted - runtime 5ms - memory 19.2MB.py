class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        l=[]
        for i in s:
            if nums.count(i)==2:
                l.append(i)
        return l