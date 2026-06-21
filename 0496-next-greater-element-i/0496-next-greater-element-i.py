class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for i in range(len(nums2)):
            d[nums2[i]]=i
        print(d)
        r=[]
        for i in nums1:
            x=-1
            for j in range(d[i],len(nums2)):
                if nums2[j]>i:
                    x=nums2[j]
                    break
            r.append(x)
        return r