class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1={}
        d2={}
        x=[]
        for i in set(nums1):
            d1[i]=nums1.count(i)
        for i in set(nums2):
            d2[i]=nums2.count(i)
        for i in d1:
            if i in d2:
                for j in range(min(d1[i],d2[i])):
                    x.append(i)
        return x
