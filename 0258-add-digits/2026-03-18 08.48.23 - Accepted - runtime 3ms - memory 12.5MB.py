class Solution(object):
    def addDigits(self, nums):
        s=0
        while len(str(nums))>1:
            s=0
            for i in str(nums):
                s+=int(i)
            nums=s
        else:
            s=nums
        return s