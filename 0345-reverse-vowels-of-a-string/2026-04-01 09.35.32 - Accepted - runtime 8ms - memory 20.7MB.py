class Solution:
    def reverseVowels(self, s: str) -> str:
        v=set("aeiouAEIOU")
        r=[]
        x=list(s)
        for i in s:
            if i in v:
                r.append(i)
        r=r[::-1]
        c=0
        for i in range(len(s)):
            if s[i] in v:
                x[i]=r[c]
                c+=1
        return "".join(x)