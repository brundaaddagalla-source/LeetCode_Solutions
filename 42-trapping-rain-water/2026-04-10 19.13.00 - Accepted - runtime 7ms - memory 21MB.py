class Solution:
    def trap(self, height: List[int]) -> int:
        l=height[0]
        i=0
        s=0
        j=len(height)-1
        r=height[-1]
        while i<j:
            if l<=r:
                s+=l-height[i]
                i+=1
                l=max(l,height[i])
            else:
                s+=r-height[j]
                j-=1
                r=max(r,height[j])
        return s