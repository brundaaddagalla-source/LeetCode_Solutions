class Solution:
    def smallestPalindrome(self, s: str) -> str:
        if len(s)==1:
            return s
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        x=""
        m=""
        for i in sorted(d):
            x+=i*(d[i]//2)
            if d[i]%2==1:
                m+=i
        r="".join(list(x)[::-1])
        return x+m+r
