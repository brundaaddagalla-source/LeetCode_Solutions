class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(nums,low,high):
            mini=float("inf")
            while low<=high:
                mid=(low+high)//2
                if nums[low]<=nums[mid]:
                    mini=min(mini,nums[low])
                    low=mid+1
                else:
                    mini=min(mini, nums[mid])
                    high=mid-1
            return mini
        return binary(nums, 0, len(nums)-1)