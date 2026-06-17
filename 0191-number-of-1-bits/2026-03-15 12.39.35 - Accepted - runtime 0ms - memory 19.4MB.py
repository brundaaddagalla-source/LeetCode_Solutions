class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)[2:]
        return x.count("1")