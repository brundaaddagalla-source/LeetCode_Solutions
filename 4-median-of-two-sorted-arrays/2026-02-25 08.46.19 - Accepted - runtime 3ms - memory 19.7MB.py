class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=nums1+nums2
        m=sorted(m)
        if len(m)%2==1:
            return m[len(m)//2]
        else:
            return (m[len(m)//2]+m[(len(m)//2)-1])/2