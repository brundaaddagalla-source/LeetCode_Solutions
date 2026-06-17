class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if i==j:
        #             continue
        #         else:
        #             if nums[i]==nums[j] and abs(i-j)<=k:
        #                 return True
        # return False
        s=set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s)>k:
                s.remove(nums[i-k])
        return False