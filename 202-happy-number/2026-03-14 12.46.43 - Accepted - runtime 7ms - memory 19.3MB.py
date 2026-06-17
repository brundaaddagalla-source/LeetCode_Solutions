class Solution:
    def isHappy(self, n: int) -> bool:
        # def sums(n):
        #     s=0
        #     for i in str(n):
        #         s+=int(i)*int(i)
        #     return s
        # if n<10 and n!=1 and n!=7:
        #     return False
        # r=sums(n)
        # while True:
        #     if r==1:
        #         return True
        #     else:
        #         if r<10 and n!=7:
        #             return False
        #         else:
        #             r=sums(r)
        c=0
        while(c<100):
            s=0
            for i in str(n):
                s+=int(i)*int(i)
            n=s
            if n==1:
                return True
            c+=1
        return False
                
            