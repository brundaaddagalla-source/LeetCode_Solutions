class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        dp={}
        ds={}
        for i in p:
            dp[i]=dp.get(i,0)+1
        left=0
        r=[]
        for i in range(len(s)):
            ds[s[i]]=ds.get(s[i],0)+1
            if i-left+1>len(p):
                ds[s[left]]-=1
                if ds[s[left]]==0:
                    del ds[s[left]]
                left+=1
            if i-left+1==len(p) and dp==ds:
                r.append(left)
        return r
