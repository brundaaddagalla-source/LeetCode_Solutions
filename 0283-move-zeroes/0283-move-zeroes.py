class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[i],nums[j]=nums[j],nums[i]
        #         j+=1
        # return nums
        i=0
        while i<len(nums):
            if nums[i]==0:
                nums.pop(i)
                j+=1
            else:
                i+=1
        nums+=[0]*j
        return nums
