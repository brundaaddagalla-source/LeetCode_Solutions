class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        c=0
        l=[]
        r=[]
        for i in nums:
            if i==pivot:
                c+=1
            elif i<pivot:
                l.append(i)
            else:
                r.append(i)
        nums=l+[pivot]*c+r
        return nums