class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        p=0
        hash={0:1}
        for i in range(len(nums)):
            p+=nums[i]
            if p-k in hash:
                c+=hash[p-k]
            hash[p]=hash.get(p,0)+1
        return c