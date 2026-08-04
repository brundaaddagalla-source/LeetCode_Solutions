class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        start=min(nums)
        end=max(nums)
        s=set(nums)
        r=[]
        for i in range(start, end+1):
            if i not in s:
                r.append(i)
        return r