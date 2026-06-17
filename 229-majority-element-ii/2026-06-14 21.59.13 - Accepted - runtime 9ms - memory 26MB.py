class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=len(nums)//3
        s=set()
        d={}
        for i in nums:
            if i in s:
                d[i]+=1
            else:
                d[i]=1
                s.add(i)
        r=[]
        for i in d:
            if d[i]>x:
                r.append(i)
        return r