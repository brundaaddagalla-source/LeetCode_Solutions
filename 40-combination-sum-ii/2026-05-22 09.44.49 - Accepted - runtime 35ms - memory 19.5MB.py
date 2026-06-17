class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s=0
        candidates.sort()
        ans=[]
        path=[]
        def backtracking(i,s):
            if s==target:
                ans.append(path[:])
                return
            if s>target or i==len(candidates):
                return
            path.append(candidates[i])
            backtracking(i+1,s+candidates[i])
            path.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtracking(i+1,s)
        backtracking(0,0)
        return ans