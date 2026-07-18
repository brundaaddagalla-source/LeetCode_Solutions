class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,path):
            r.append(path)
            for i in range(start, len(nums)):
                backtrack(i+1, path+[nums[i]])
        r=[]
        backtrack(0,[])
        return r
