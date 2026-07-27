class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=nums[:n]
        y=nums[n:]
        r=[]
        for i in range(n):
            r.append(x[i])
            r.append(y[i])
        return r