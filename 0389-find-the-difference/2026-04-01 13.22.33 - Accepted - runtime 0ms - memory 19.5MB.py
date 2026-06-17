class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if set(s)!=set(t):
            x=set(t)-set(s)
            x="".join(x)
            return x
        else:
            for i in set(t):
                if t.count(i)-s.count(i)==1:
                    return i
                    