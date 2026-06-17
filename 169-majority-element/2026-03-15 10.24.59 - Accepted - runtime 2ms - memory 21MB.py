class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen=set(nums)
        max=-float("inf")
        n=len(nums)
        for i in seen:
            if nums.count(i)>(n//2) and i>max:
                max=i
        return max