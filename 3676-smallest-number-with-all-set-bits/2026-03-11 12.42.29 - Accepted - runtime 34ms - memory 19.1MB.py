class Solution:
    def smallestNumber(self, n: int) -> int:
        f=1
        while f:
            b=bin(n)[2:]
            if all(i=='1' for i in b):
                f=0
                return n
            else:
                n+=1