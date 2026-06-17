class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={0:0,1:0,2:0}
        for i in nums:
            d[i]+=1
        nums[:]=d[0]*[0]+d[1]*[1]+d[2]*[2]