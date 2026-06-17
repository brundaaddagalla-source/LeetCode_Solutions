class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            si=1
        else:
            si=0
        x=abs(x)
        x=int(str(x)[::-1])
        if si==1:
            x=-x
        if x>=(-2**31) and x<=(2**31)-1:
            return x
        else:
            return 0