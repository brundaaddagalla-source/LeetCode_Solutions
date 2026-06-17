class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def check(s):
            if len(s)==2:
                return s[0]==s[1]
            ts=""
            for i in range(len(s)-1):
                r=(int(s[i])+int(s[i+1]))%10
                ts+=str(r)
            return check(ts)
        return check(s)