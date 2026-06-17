class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num=set(nums)
        return nums.index(max(num))