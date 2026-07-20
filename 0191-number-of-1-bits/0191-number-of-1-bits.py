class Solution:
    def hammingWeight(self, n: int) -> int:
        # x=bin(n)[2:]
        # return x.count("1")
        c=0
        #this loop will run for 32 times cuz integer is represented in 32 bits
        for i in range(32):
            x=n>>i #shifting the value right
            if x&1: #checking if the last bit is one or not
                c+=1
        return c
