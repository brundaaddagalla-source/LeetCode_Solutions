class Solution:
    def minimumPushes(self, word: str) -> int:
        c=0
        i=1
        n=len(word)
        while n>0:
            if n>=8:
                c+=(i*8)
                n-=8
            else:
                c+=(i*n)
                n-=n
            i+=1
        return c