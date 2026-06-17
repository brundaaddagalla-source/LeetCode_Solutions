class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r=[]

        def dfs(o,c,s):
            if o==c and o+c==n*2:
                r.append(s)
                return 
            if o<n:
                dfs(o+1,c,s+"(")
            if c<o:
                dfs(o,c+1,s+")")
        dfs(0,0,"")
        return r