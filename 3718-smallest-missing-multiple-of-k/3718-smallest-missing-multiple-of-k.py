class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            if k*i not in nums:
                break
            i+=1
        return k*i