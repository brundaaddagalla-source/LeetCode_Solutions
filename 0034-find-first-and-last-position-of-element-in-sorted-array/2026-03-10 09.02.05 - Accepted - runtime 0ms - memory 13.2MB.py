class Solution(object):
    def searchRange(self, nums, target):
        def first(nums,target):
            start=0
            f=0
            r=-1
            end=len(nums)-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    r=mid
                    end=mid-1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return r
        def last(nums,target):
            start=0
            f=0
            r=-1
            end=len(nums)-1
            while start<=end:
                mid=(start+end)//2
                if nums[mid]==target:
                    r=mid
                    start=mid+1
                elif nums[mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return r
        return [first(nums,target),last(nums,target)]
            