class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        curr = 1
        ans = 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr += 1
            else:
                ans = max(ans, min(prev,curr), curr//2)
                prev = curr
                curr = 1
        ans = max(ans, min(prev,curr), curr//2)
        return ans