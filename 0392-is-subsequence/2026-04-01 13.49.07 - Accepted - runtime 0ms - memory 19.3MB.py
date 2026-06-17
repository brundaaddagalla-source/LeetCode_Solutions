class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        x=""
        j=0
        for i in t:
            if j<len(s) and s[j]==i :
                j+=1
                x+=i
        if x==s:
            return True
        else:
            return False