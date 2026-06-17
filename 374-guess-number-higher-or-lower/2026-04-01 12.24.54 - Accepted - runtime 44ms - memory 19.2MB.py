# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            s=(low+high)//2
            x=guess(s)
            if x==0:
                return s
            elif x==1:
                low=s+1
            else:
                high=s-1
