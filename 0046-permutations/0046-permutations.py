class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r=[]
        path=[]
        u=[0]*len(nums)
        def backtrack():
            if len(path)==len(nums):
                r.append(path[:])
                return 
            for i in range(len(nums)):
                if u[i]:
                    continue
                path.append(nums[i])
                u[i]=1
                backtrack()
                path.pop()
                u[i]=0
        backtrack()
        return r
                

            