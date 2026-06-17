class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.p=[0]
        for i in range(len(self.nums)):
            self.p.append(self.nums[i]+self.p[-1])

    def sumRange(self, left: int, right: int) -> int:
        # return sum(self.nums[left:right+1])
        return self.p[right+1]-self.p[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)