class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if sorted(s)==sorted(t):
        #     return True
        # else:
        #     return False
        if len(s)!=len(t):
            return False
        else:
            for i in "abcdefghijklmnopqrstuvwxyz":
                if s.count(i)!=t.count(i):
                    return False
        return True