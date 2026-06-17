class Solution:
    def search(self, a: List[int], target: int) -> int:
        low=0
        high=len(a)-1
        while low<=high:
            mid=low+(high-low)//2
            if a[mid]==target:
                return mid
            elif a[low]<=a[mid]:
                if a[low]<=target<=a[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if a[mid]<=target<=a[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1