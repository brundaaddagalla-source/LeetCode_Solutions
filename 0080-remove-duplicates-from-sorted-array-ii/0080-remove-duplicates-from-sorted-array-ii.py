class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d={}
        k=0
        i=0
        while i <len(nums):
            d[nums[i]]=d.get(nums[i], 0)+1
            if d[nums[i]]>2:
                nums.pop(i)
            else:
                i+=1
        return len(nums)