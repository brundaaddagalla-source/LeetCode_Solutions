class Solution:
    def reverseBits(self, n: int) -> int:
        # x=bin(n)[2:].zfill(32)
        # x=x[::-1]
        # return int(x,2)
        ans=0
        for i in range(32):
            x=n&1 #extract the last bit from the number
            ans=ans<<1 #shifting the bits by 1 position to make place for the bit extracted
            ans=ans|x #appending the extracted bit
            n>>=1 #moving onto the next bit
        return ans