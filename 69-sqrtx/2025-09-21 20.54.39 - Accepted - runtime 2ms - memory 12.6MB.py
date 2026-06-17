class Solution(object):
    import math
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        y=sqrt(x)
        return int(math.floor(y))