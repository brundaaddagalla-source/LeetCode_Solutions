class Solution:
    def toHex(self, n: int) -> str:
        d={10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        s=""
        if n==0:
            return "0"
        if n<0:
            n=n+(2**32)
        while n>0:
            q=n%16
            if q>=10:
                s+=d[q]
            else:
                s+=str(q)
            n=n//16

        return s[::-1]