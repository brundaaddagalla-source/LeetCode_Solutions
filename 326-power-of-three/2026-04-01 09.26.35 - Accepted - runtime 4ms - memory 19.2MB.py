class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # f=1
        # c=0
        # while True:
        #     if 3**c==n:
        #         return True
        #     elif 3**c > n:
        #         return False
        #     c+=1
        # return False
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1