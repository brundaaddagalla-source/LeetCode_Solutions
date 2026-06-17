class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        f={}
        c=[0]*len(A)
        for i in range(len(A)):
            if A[i] not in f:
                f[A[i]]=1
            else:
                f[A[i]]+=1
            if B[i] not in f:
                f[B[i]]=1
            else:
                f[B[i]]+=1
            x=list(f.values())
            c[i]=x.count(2)
        return c