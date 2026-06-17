class Solution:
    def arrangeCoins(self, n: int) -> int:
        level=0
        while level+1<=n:
            level+=1
            n-=level
        return level