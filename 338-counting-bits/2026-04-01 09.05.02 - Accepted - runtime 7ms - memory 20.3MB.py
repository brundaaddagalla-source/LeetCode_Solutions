class Solution:
    def countBits(self, n: int) -> List[int]:
        x=[]
        for i in range(n+1):
            y=bin(i)[2:]
            x.append(y.count("1"))
        return x