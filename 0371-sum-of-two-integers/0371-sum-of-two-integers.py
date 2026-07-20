class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask=0xFFFFFFFF
        max_int=0x7FFFFFFF
        
        while b!=0:
            carry=((a&b)<<1)&mask #finding out the carry value
            sums=(a^b)&mask #finding out the sum value
            a=sums
            b=carry
        
        #here a is an unsigned integer, so when a is negative, we are performing 2's complement
        return a if a<=max_int else ~(a^mask) #return a if a is positive or return the 2's complement
        