class Solution(object):
    def summaryRanges(self, nums):
        i=0
        r=[]
        while i<len(nums):
            start=i
            while i+1<len(nums) and nums[i+1]==nums[i]+1:
                i+=1
            else:
                if start==i:
                    r.append(str(nums[i]))
                    i+=1
                else:
                    s=str(nums[start])+"->"+str(nums[i])
                    r.append(s)
                    i+=1
                    start=i
        return r
