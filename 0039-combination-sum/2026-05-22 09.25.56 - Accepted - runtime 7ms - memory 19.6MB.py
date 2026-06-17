class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s=0
        ans=[]
        path=[]
        def backtracking(i,s):
            if s==target:
                ans.append(path[:])
                return
            if s>target or i==len(candidates):
                return
            path.append(candidates[i])
            backtracking(i,s+candidates[i])
            path.pop()
            backtracking(i+1,s)
        backtracking(0,0)
        return ans