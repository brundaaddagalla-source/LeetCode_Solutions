class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # f=1
        # c=0
        # while True:
        #     if 4**c==n:
        #         return True
        #     elif 4**c > n:
        #         return False
        #     c+=1
        # return False
        if n<=0:
            return False
        while n%4==0:
            n//=4
        return n==1