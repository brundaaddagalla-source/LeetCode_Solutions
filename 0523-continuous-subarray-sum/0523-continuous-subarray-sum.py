class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums)<2:
            return False
        prefix=[nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1]+nums[i])
        for i in range(1,len(prefix)):
            if prefix[i]%k==0:
                return True
        # for i in range(len(prefix)):
        #     for j in range(i+2,len(prefix)):
        #         if (prefix[j]-prefix[i])%k==0:
        #             return True
        d={}
        for i in range(len(prefix)):
            r=prefix[i]%k
            if r in d:
                if i-d[r]>=2:
                    return True
            else:
                d[r]=i
        return False