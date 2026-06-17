class Solution(object):
    def divide(self, dividend, divisor):
        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            s=1
        else:
            s=-1
        dividend=abs(dividend)
        divisor=abs(divisor)
        r=dividend//divisor
        r=s*r
        if r > 2**31 - 1:
            return 2**31 - 1
        if r < -2**31:
            return -2**31
        return r
        