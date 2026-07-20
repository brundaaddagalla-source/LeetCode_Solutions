class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n==1:
            return [0,1]
        x=1<<n
        r=[0]*x
        for i in range(x):
            r[i]=i^(i>>1)
        return r
        
