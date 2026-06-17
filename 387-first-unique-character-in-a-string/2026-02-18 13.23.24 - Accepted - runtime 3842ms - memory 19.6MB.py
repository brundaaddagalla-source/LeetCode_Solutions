class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=[]
        x=s[0]
        for i in range(len(s)):
            if s.count(s[i])==1:
                return i
        return -1