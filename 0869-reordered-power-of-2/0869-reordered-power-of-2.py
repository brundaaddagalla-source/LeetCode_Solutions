class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n="".join(sorted(list(str(n))))
        ans=False
        for i in range(30): #2**30>10**9
            if "".join(sorted(list(str(2**i))))==n:
                ans=True
                break
        return ans