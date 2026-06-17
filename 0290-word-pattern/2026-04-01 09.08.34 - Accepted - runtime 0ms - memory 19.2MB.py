class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split()
        if len(pattern)!=len(w):
            return False
        seen={}
        for i,j in zip(pattern, w):
            key_p=("p",i)
            key_w=("w",j)
            if key_p in seen and seen[key_p]!=key_w:
                return False
            if key_w in seen and seen[key_w]!=key_p:
                return False
            seen[key_p]=key_w
            seen[key_w]=key_p
        return True