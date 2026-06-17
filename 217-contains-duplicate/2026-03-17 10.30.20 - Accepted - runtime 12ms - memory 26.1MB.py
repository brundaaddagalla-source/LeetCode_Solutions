class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen=set(nums)
        # for i in seen:
        #     if nums.count(i)>1:
        #         return True
        # return False
        if len(list(seen))==len(nums):
            return False
        else:
            return True