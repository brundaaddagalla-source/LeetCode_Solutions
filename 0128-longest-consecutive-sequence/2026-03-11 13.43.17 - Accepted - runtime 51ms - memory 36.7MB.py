class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        f = set(nums)
        c = 0
        for i in f:
            if i - 1 not in f:   # start of sequence
                curr = i
                l = 1
                while curr + 1 in f:
                    curr += 1
                    l += 1
                c = max(c, l)
        return c