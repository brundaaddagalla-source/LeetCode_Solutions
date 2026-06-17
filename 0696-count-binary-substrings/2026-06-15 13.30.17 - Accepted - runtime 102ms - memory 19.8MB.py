class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        i=0
        r=[]
        while i<=len(s)-1:
            c=1
            while i+1<len(s) and s[i]==s[i+1]:
                c+=1
                i+=1
            r.append(c)
            i+=1
        t=0
        for i in range(len(r)-1):
            t+=min(r[i],r[i+1])
        return t