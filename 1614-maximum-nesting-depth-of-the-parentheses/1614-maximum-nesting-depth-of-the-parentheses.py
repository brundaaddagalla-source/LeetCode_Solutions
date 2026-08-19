class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=-1
        c=0
        for i in s:
            if i==")":
                maxi=max(c, maxi)
                c-=1
            elif i=="(":
                c+=1
        return maxi if maxi>0 else 0