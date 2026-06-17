class Solution:
    def findMin(self, nums: List[int]) -> int:
        # low=0
        # high=len(nums)-1
        # while low<high:
        #     mid=(low+high)//2
        #     if nums[mid]==nums[low] and nums[mid]==nums[high]:
        #         low+=1
        #         high-=1
        #     elif nums[mid]<=nums[high]: high=mid
        #     else: low=mid+1
        # return nums[low]
        return min(nums)